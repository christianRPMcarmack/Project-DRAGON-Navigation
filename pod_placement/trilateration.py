import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd
import scipy

sns.set()
sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}

# matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
# plt.style.use('fivethirtyeight')

pods = (
    (10, 40), 
    (50, 20),
    (40, 80),
)

### Note: When doing this with coordinates, use 'great_circle_distance'

measured_distances = (30, 25, 37)

def position_error(x, pod_locations, measured_distances):
    mse = 0
    for location, distance in zip(pod_locations, measured_distances):
        calculated_distance = np.sqrt( (x[0] - location[0]) ** 2 + (x[1] - location[1]) ** 2)
        mse += (calculated_distance - distance) ** 2

    return mse / len(pods)

initial_guess = (30, 40) # actual is about (40, 42)

result = scipy.optimize.minimize(
        position_error, # error in estimate, minimizing
        initial_guess, 
        args=(pods, measured_distances),
        )

print(result)
