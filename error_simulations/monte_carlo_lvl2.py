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

from trilateration_eqns import x_independent, y_independent, x_upper, y_upper, trilateration_error

SIZE = 100

path_x = np.concatenate((np.linspace(0, SIZE, SIZE), np.linspace(100, 200, 100)))
path_y = np.concatenate((np.linspace(0, SIZE, SIZE), SIZE * np.ones(100)))

pods = [
    (10, 0),
    (0, 10),
    (20, 10),
    (20, 30),
    (40, 30),
    (40, 50),
    (60, 50),
    (60, 70),
    (80, 70),
    (80, 90),
    (100, 90),
    (50, 110),
]

deployment_indices = [0, 0, 10, 20, 30, 40, 50, 60, 70, 80, 110]

def sim():
    ## Randomly place pods

    # pods = []

    #deployment_indices = []

    #while len(pods) < 10:
    #   index = np.random.randint(0, SIZE)
    #    location = (path_x[index] + np.random.choice([-1, 1]) * np.random.randint(5, 20),
    #                path_y[index] + np.random.choice([-1, 1]) * np.random.randint(5, 20))

    #    if any(np.array(location) < 0) or any(np.array(location) > SIZE):
    #        continue
    #    else:
    #        pods.append(location)
    #        deployment_indices.append(index)
            # pods_error.append((.1, .1))
            
    # initialize error in rover
    rover_error = np.array([.1, .1])
    rover_independent_error_log = []

    # Starts same
    rover_upper_error_log = []

    # Increase in rover error if not within range of >= 3 pods
    ROVER_IMU_ERROR = [.01, .01] # .01 is _super_ optimistic

    # x, y error in pod deployment. Update with theta/alpha/rho later
    DEPL_ERROR = .00 # [ m ]

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
        pods_range = np.array([np.sqrt( (x - pod[0]) ** 2 + (y - pod[1]) ** 2) for pod in deployed_pods])
        
        
    #     If >= 3 pods, get trilateration error from position
        if (pods_range < POD_RANGE).sum() >= 3:
            nearest_pods_indices = np.array(pods_range).argsort()[:3]
            pods_in_range = [deployed_pods[i] for i in nearest_pods_indices]
            pods_in_range_error = [pods_error[i] for i in nearest_pods_indices] 
            measured_range = [pods_range[i] for i in nearest_pods_indices]
            measured_range_error = [RANGE_ERROR * dist for dist in measured_range]
            
            print(pods_in_range, pods_in_range_error, measured_range, measured_range_error)
            x_independent_error, y_independent_error, x_upper_error, y_upper_error = trilateration_error(pods_in_range, pods_in_range_error, measured_range, measured_range_error)
    #         Error from trilat is new rover error
            # print(x_independent_error, pods_in_range_error, error_of_range_of_pods_in_range)
            rover_independent_error_log.append((x_independent_error, y_independent_error))
            rover_upper_error_log.append((x_upper_error, y_upper_error)) 
            rover_error = np.array((x_independent_error, y_independent_error))
            
        else: # if not enough pods to trilaterate
            rover_error += ROVER_IMU_ERROR
            rover_independent_error_log.append(list(rover_error))
            rover_upper_error_log.append(list(rover_error))
        #print('\n')

    rover_independent_error_log = np.array(rover_independent_error_log)
    rover_upper_error_log = np.array(rover_upper_error_log)

    rover_independent_error_log_max = rover_independent_error_log.max(axis=1)
    rover_upper_error_log_max = rover_upper_error_log.max(axis=1) 
    
    return rover_independent_error_log_max, rover_upper_error_log_max 

iterations = 1

independent_error = np.zeros((iterations, len(path_x)))
upper_error = np.zeros((iterations, len(path_x)))

for i in range(iterations):
    print(i)
    ind_error, upp_error = sim()
    independent_error[i] = ind_error
    upper_error[i] = upp_error
    

independent_error = np.nan_to_num(independent_error, 0)
upper_error = np.nan_to_num(upper_error, 0)

independent_error = independent_error.mean(axis=0)
upper_error = upper_error.mean(axis=0)


plt.figure(figsize=(10,10))
plt.plot(range(len(path_x)), independent_error, label='Lower Bound')
plt.plot(range(len(path_x)), upper_error, label='Upper Bound')
plt.ylabel('Position ${\\tt max } \sigma [ m ]$')
plt.xlabel('Rover Along-Track Distance [ m ]')
plt.legend()

plt.tight_layout()
plt.savefig('error_plot.png')
plt.show()

plt.plot(*zip(*pods), marker='.', linestyle='None', label='Pod', markersize=20)
plt.plot(path_x, path_y, marker='.', linestyle='None', label='Rover Path', markersize=7)
plt.plot(path_x[deployment_indices], path_y[deployment_indices], marker='.', linestyle='None', label='Deployment', markersize=15, color='g')
plt.ylabel('$y$ [ m ]')
plt.xlabel('$x$ [ m ]')
plt.legend()

plt.tight_layout()
plt.savefig('map.png')
plt.show()


#f, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
#f.set_figheight(15)
#f.set_figwidth(10)

#ax1.plot(*zip(*pods), marker='.', linestyle='None', label='Pod', markersize=20)
#ax1.plot(path_x, path_y, marker='.', linestyle='None', label='Rover Path', markersize=7)
#ax1.plot(path_x[deployment_indices], path_y[deployment_indices], marker='.', linestyle='None', label='Deployment', markersize=15, color='g')
#ax1.set_ylabel('Rover $y$ Position [ m ]')
#ax1.set_xlabel('Rover $x$ Position [ m ]')
#ax1.legend()

#ax2.plot(path_x, independent_error, label='Lower Bound')
#ax2.plot(path_x, upper_error, label='Upper Bound')

#ax2.set_ylabel('Position ${\\tt max } \sigma [ m ]$')
#ax2.set_xlabel('Rover $x$ Position [ m ]')
#ax2.legend()

#plt.tight_layout()
#plt.savefig('error_plot.png')
#plt.show()
