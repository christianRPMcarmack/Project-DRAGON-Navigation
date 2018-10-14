import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from math import *
import pandas as pd
import subprocess as sp
import ast

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}

matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
plt.style.use('fivethirtyeight')

def write_sage_cfg(pod_locations, pods_error, ranges, range_errors):
    with open('trilateration.parameters', 'w') as f:
        f.write(str(pod_locations) + '\n\n')
        f.write(str(pods_error) + '\n\n')
        f.write(str(ranges) + '\n\n')
        f.write(str(range_errors) + '\n\n')
    
    return
    
def run_sage():
    ret = sp.run('sage trilateration_error.sage', shell=True, stdout=sp.PIPE)
    
    print(ret.stdout.decode())
    ret_worst, ret_independent = ast.literal_eval(ret.stdout.decode().strip())

    return ret_worst, ret_independent

## Randomly place pods
SIZE = 100

path_x = np.linspace(0, SIZE, SIZE)
path_y = np.linspace(0, SIZE, SIZE)

pods = []

deployment_indices = []

while len(pods) < 10:
    index = np.random.randint(0, SIZE)
    location = (path_x[index] + np.random.choice([-1, 1]) * np.random.randint(5, 20),
                path_y[index] + np.random.choice([-1, 1]) * np.random.randint(5, 20))

    if any(np.array(location) < 0) or any(np.array(location) > SIZE):
        continue
    else:
        pods.append(location)
        deployment_indices.append(index)
        # pods_error.append((.1, .1))
        
# initialize error in rover
rover_error = np.array([.1, .1])
rover_error_log = []

# Starts same
rover_error_log_worst = []

# Increase in rover error if not within range of >= 3 pods
ROVER_IMU_ERROR = [.01, .01] # .01 is _super_ optimistic

# x, y error in pod deployment. Update with theta/alpha/rho later
DEPL_ERROR = .15 # [ m ]

# range ot which pods are able to be used
POD_RANGE = 100 # [ m ]

# Error in pod ranging measurement 
RANGE_ERROR = .01

deployed_pods = []

pods_error = []

# for each location
for path_index, x, y in zip(range(len(path_x)), path_x, path_y):
    print(path_index, x, y)
#     If pod needs to be deployed, deploy pod
    if path_index in deployment_indices:
        # Sometimes there are repeats, do all of them here
        for pod_index in [i for i, e in enumerate(deployment_indices) if e == path_index]:
#         Add error from rover to error in depl
            deployed_pods.append(pods[pod_index])
#         Assume constant x, y error for now, add theta/alpha/rho later
            pods_error.append(list(rover_error + [DEPL_ERROR, DEPL_ERROR]))
#     Check distance to all pods
    pods_range = [np.sqrt( (x - pod[0]) ** 2 + (y - pod[1]) ** 2) for pod in deployed_pods]
    
    pods_in_range_indices = [i for i, e in enumerate(pods_range) if e < POD_RANGE]
    
#     If >= 3 pods, get trilateration error from position
    if len(pods_in_range_indices) >= 3:
        pods_in_range = [deployed_pods[i] for i in pods_in_range_indices]
        pods_in_range_error = [pods_error[i] for i in pods_in_range_indices]
        range_of_pods_in_range = [pods_range[i] for i in pods_in_range_indices]
        error_of_range_of_pods_in_range = [.01 * dist for dist in range_of_pods_in_range]
#         Call sage with pod location, distance, and pod error
        write_sage_cfg(list(pods_in_range), pods_in_range_error, 
                       range_of_pods_in_range, error_of_range_of_pods_in_range)
#         Error from sage is new rover error
        rover_error_worst, rover_error = run_sage()
        rover_error_log.append(rover_error)
        rover_error_log_worst.append(rover_error_worst)
        rover_error = np.array(rover_error)
        
    else: # if not enough pods to trilaterate
        rover_error += ROVER_IMU_ERROR
        rover_error_log.append(list(rover_error))
        rover_error_log_worst.append(list(rover_error))
    print('\n')

rover_error_log = np.array(rover_error_log)
rover_error_log_worst = np.array(rover_error_log_worst)

f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
f.set_figheight(15)
f.set_figwidth(15)

ax1.plot(*zip(*pods), marker='.', linestyle='None', label='Pod', markersize=20)
ax1.plot(path_x, path_y, marker='.', linestyle='None', label='Rover', markersize=7)
ax1.plot(path_x[deployment_indices], path_y[deployment_indices], marker='.', linestyle='None', label='Deployment Location', markersize=15, color='g')
ax1.set_ylabel('Rover $y$ Position [ m ]')
ax1.set_xlabel('Rover $x$ Position [ m ]')

ax2.plot(path_x, rover_error_log.max(axis=1), label='Lower Bound')
ax2.plot(path_x, rover_error_log_worst.max(axis=1), label='Upper Bound')

ax2.set_ylabel('$Position {\\tt max} \sigma [ m ]$')
ax2.set_xlabel('Rover $x$ Position [ m ]')
ax2.legend()

plt.tight_layout()
plt.savefig('error_plot.png')
plt.show()

