import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd
import scipy.optimize

sns.set()
sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}

# matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
# plt.style.use('fivethirtyeight')

distance_func = lambda x1, y1, x2, y2 : np.sqrt( ( x1 - x2) ** 2 + (y1 - y2) ** 2)



def within_bounds(x, y):
    if (x < 0) or (x > 200):
        return False

    if (y < 0) or (y > 200):
        return False
    # This is so inefficient that it makes me cry
    distance_vec = []

    for func_x, func_y in zip(x_span, func_values):
        distance = distance_func(func_x, func_y, x, y)
        distance_vec.append(distance)

    distance_vec = np.array(distance_vec)

    if np.any(distance_vec < 5):
        return False

    if np.all(distance_vec > 20):
        return False

    return True

def q_matrix(x, y, pods):
    range_func = lambda pod_number : np.sqrt( (pods[pod_number][0] - x) ** 2 + (pods[pod_number][1] - y) ** 2 )

    A = np.zeros([len(pods), 3])

    for i, coords in enumerate(pods):
        A[i] = [ (coords[0] - x) / range_func(i), (coords[1] - y) / range_func(i), -1 ]
    
    # A[np.isnan(A)] = 1000
    try:
        Q = np.linalg.inv(np.matmul(A.T , A))
    except:
        return np.array([[1000],])
    
    return Q

def dop_map(x_span, y_span, pods):
    DOP = np.zeros([len(x_span), len(y_span)])

    for xi, x in enumerate(x_span):
        for yi, y in enumerate(y_span):
            DOP[xi][yi] = np.sqrt(np.trace(q_matrix(x, y, pods)))

    DOP = np.log(DOP.T)

    return DOP


def figure_of_merit(pods_vec, x_span, y_span, path_function):
    pods = np.array(pods_vec).reshape(-1, 2)
    print(pods)
    for pod in pods:
        if not within_bounds(pod[0], pod[1]):
            print('oob', pod)
            # Want to weight really badly so no pods out of bounds
            return 10e6
    
    DOP = dop_map(x_span, y_span, pods)
    
    FOM = 0

    for x in x_span:
        y = np.int(path_function(x))
        FOM += DOP[x][y]
    
    print(FOM)
    return FOM

pods_initial = [
    [30, 15],
    [100, 40],
    [160, 138],
    [180, 145],
]

x_span = np.arange(0, 200)
y_span = np.arange(0, 200)

path_func = lambda x: .005 * x ** 2
func_values = np.array(list(map(path_func, x_span)))

# figure_of_merit(np.ravel(pods_initial), x_span, y_span, path_func)

DOP = dop_matrix(x_span, y_span, pods_initial)

plt.figure(figsize=(9, 11))
plt.matshow(DOP)
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_bottom()
plt.colorbar(label='$\\texttt{DOP}$')
plt.plot(.005 * x_span ** 2, color='g')
plt.scatter(*zip(*pods_initial))
plt.xlabel('$x$ [ m ]') 
plt.ylabel('$y$ [ m ]') 
plt.tight_layout()
plt.savefig('initial.png', bbox_inches = 'tight')
plt.close

result = scipy.optimize.minimize(
        figure_of_merit,
        np.ravel(pods_initial), 
        args=(x_span, y_span, path_func),
)



# plt.imshow(map_path)
# plt.gca().invert_yaxis()
# plt.show()
