import numpy as np
from scipy.optimize import minimize


def position_error(x, pod_locations, measured_distances):
    mse = 0
    for location, distance in zip(pod_locations, measured_distances):
        calculated_distance = np.sqrt( (x[0] - location[0]) ** 2 + (x[1] - location[1]) ** 2)
        mse += (calculated_distance - distance) ** 2

    return mse / len(pod_locations)

# https://www.alanzucconi.com/2017/03/13/positioning-and-trilateration/
def trilaterate(x, pod_locations):
    calculated_distances = []
    
    for location in pod_locations:
        calculated_distances.append(np.sqrt( (x[0] - location[0]) ** 2 + (x[1] - location[1]) ** 2))
    
        
    result = minimize(
        position_error, # error in estimate, minimizing
        (0, 0), # Initial guess: will need to update at some point, but (0, 0) should work
        args=(pod_locations, calculated_distances),
        )
        
    return result.x


## FIX ME
def trilaterate_with_error(x, pod_locations, variance):
    for location in pod_locations:
        calculated_distance = np.sqrt( (x[0] - location[0]) ** 2 + (x[1] - location[1]) ** 2)
        distance_with_error = calculated_distance + np.random.normal(0, variance)
        
    result = minimize(
        position_error, # error in estimate, minimizing
        initial_guess = (0, 0), # Will need to update at some point, but (0, 0) should work
        args=(pods, measured_distances),
        )
        
    return result.x
