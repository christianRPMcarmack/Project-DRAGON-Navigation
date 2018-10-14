import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd

sns.set()
sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}

# matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
# plt.style.use('fivethirtyeight')


pods = [
    [30, 50],
    [150, 50],
    [100, 100],
    # [160, 180],
]

def q_matrix(x, y):
    range_func = lambda pod_number : np.sqrt( (pods[pod_number][0] - x) ** 2 + (pods[pod_number][1] - y) ** 2 )

    A = np.zeros([len(pods), 3])

    for i, coords in enumerate(pods):
        A[i] = [ (coords[0] - x) / range_func(i), (coords[1] - y) / range_func(i), -1 ]
    
    # A[np.isnan(A)] = 1000
    try:
        Q = np.linalg.inv(np.matmul(A.T , A))
    except:
        print('bad')
        return np.array([[1000],])
    
    return Q

def dop_matrix(x_span, y_span):
    DOP = np.zeros([len(x_span), len(y_span)])

    for xi, x in enumerate(x_span):
        for yi, y in enumerate(y_span):
            DOP[xi][yi] = np.sqrt(np.trace(q_matrix(x, y)))

    DOP = np.log(DOP.T)

    return DOP


def figure_of_merit(DOP, x_span, path_function):
    FOM = 0

    for x in x_span:
        y = np.int(path_function(x))
        FOM += DOP[x][y]

    return FOM
    

path_function = lambda x : .005 * x ** 2

x_span = np.arange(0, 200)
y_span = np.arange(0, 200)

DOP = dop_matrix(x_span, y_span)
print(DOP)
print(figure_of_merit(DOP, x_span, path_function))

plt.figure(figsize=(9, 11))
plt.matshow(DOP)
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_bottom()
plt.colorbar(label='$\log\\texttt{DOP}$')
plt.plot(.005 * x_span ** 2, color='g')
plt.scatter(*zip(*pods))
plt.xlabel('$x$ [ m ]') 
plt.ylabel('$y$ [ m ]') 
plt.tight_layout()
plt.savefig('initial.png', bbox_inches = 'tight')
plt.close()

import sys; sys.exit(0)

for i in range(25):
    print(pods)
    DOP = dop_matrix(x_span, y_span)
    current_FOM = figure_of_merit(DOP, x_span, path_function)
    best_FOM = current_FOM
    shift_pod = 0
    shift_axis = 0
    shift_direction = 0

    for pod_num in range(len(pods)):
        for axis in [0, 1]:
            for direction in [-1, 1]:
                pods[pod_num][axis] += direction * 1
                DOP = dop_matrix(x_span, y_span) 
                FOM = figure_of_merit(DOP, x_span, path_function)
                if FOM < best_FOM:
                    best_FOM = FOM
                    shift_pod = pod_num
                    shift_axis = axis
                    shift_direction = direction

                pods[pod_num][axis] -= direction * 1


    if best_FOM < current_FOM:
        pods[shift_pod][shift_axis] += shift_direction * 1


DOP = dop_matrix(x_span, y_span)
print(figure_of_merit(DOP, x_span, path_function))

plt.figure(figsize=(9, 11))
plt.matshow(DOP)
plt.gca().invert_yaxis()
plt.gca().xaxis.tick_bottom()
plt.colorbar(label='$\log\\texttt{DOP}$')
plt.plot(.005 * x_span ** 2, color='g')
plt.scatter(*zip(*pods))
plt.xlabel('$x$ [ m ]') 
plt.ylabel('$y$ [ m ]') 
plt.tight_layout()
plt.savefig('final.png', bbox_inches = 'tight')
plt.close()
     
