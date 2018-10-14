import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd
from scipy.io import loadmat
from scipy.stats import multivariate_normal
from trilateration import trilaterate
from matplotlib.animation import FuncAnimation


sns.set()
sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}


plt.rc('text', usetex=True)

## Define map
# map_array = loadmat('map.mat')['map']

## Pod Locations 
pods = (
    (100, 400), 
    (700, 200),
    (400, 600),
)


def update_posterior(rover_pose, rover_uncertainty, ut, prior_dist):
    rover_pose += ut
    
    p_update = np.roll(prior_dist, np.array([ut[0] // 1 + np.random.choice([0, 1], p=[ut[0] % 1, 1 - ut[0] % 1]), 
                                             ut[1] // 1 + np.random.choice([0, 1], p=[ut[1] % 1, 1 - ut[1] % 1])], dtype=np.int))

    p_update += normal_array(rover_pose, np.diag(np.random.normal(800, (1, 2)))) 
        
    return rover_pose, p_update


def update_measurement(rover_pose, p_update):
    z_t = trilaterate(rover_pose, pods)
    
    p_t = normal_array(rover_pose, np.diag([200., 200.])) * p_update
    
    p_t /= p_t.sum()
    
    return p_t


def normal_array(mean, cov):
    z = multivariate_normal.pdf(list(zip(xx.ravel(), yy.ravel())), mean=mean, cov=cov)
    z.shape = (1200, 1200) 
    return z

path_direction = lambda index : np.array([1, 2/1100 * (index + .5)])


## Tile Map

x = np.arange(1200)
y = np.arange(1200)
xx, yy = np.meshgrid(x, y)


### NAVIGATION

rover_pose = np.array([100., 100.])
initial_uncertainty = np.array([800., 800.])

initial_belief = multivariate_normal.pdf(list(zip(xx.ravel(), yy.ravel())), 
                                         mean=rover_pose, cov=np.diag(initial_uncertainty))
initial_belief.shape = (1200, 1200)

prior_dist = initial_belief

for index, position in enumerate(x[:-100]):
    print(index)
    ut = path_direction(position)
    rover_pose, p_update = update_posterior(rover_pose, initial_uncertainty, ut, prior_dist)
    
    prior_dist = update_measurement(rover_pose, p_update)
    
    fig = plt.figure(figsize=(8,8))
    plt.imshow(prior_dist)
    plt.gca().invert_yaxis()
    plt.savefig('images/{}.png'.format(index))
    plt.close()


#for i in range
                

#z = multivariate_normal.pdf(list(zip(xx.ravel(), yy.ravel())), mean=mean[0], cov=cov[0])
#z.shape = (100, 100)

#fig, ax = plt.subplots()
#ax.set_xlim(0, 100)
#ax.set_ylim(0, 100)
# contour = plt.contourf(x, y, z)
#ln, = plt.plot([], [], 'ro', animated=True)


#def update(frame):
#    ax.clear()
#    z = multivariate_normal.pdf(list(zip(xx.ravel(), yy.ravel())), mean=mean[frame], cov=cov[frame])
#    z.shape = (100, 100)
#    plt.imshow(z)
    
    # Trilateration
#    tri_x, tri_y = trilaterate((mean[frame][0], mean[frame][1]), pods)
#    print(tri_x, tri_y)
#    tri_z = multivariate_normal.pdf(list(zip(xx.ravel(), yy.ravel())), mean=(tri_x, tri_y), cov=np.diag([1, 1]))
#    tri_z.shape = (100, 100)
#    plt.imshow(tri_z)
    
    # Path, pods, and rover
#    [plt.plot(pod[0], pod[1], 'bo') for pod in pods]
#    ax.plot(mean[frame][0], mean[frame][1], 'go')
#    plt.gca().invert_yaxis()
#    ln.set_data(mean[frame])

#ani = FuncAnimation(fig, update, frames=list(range(len(x))), blit=False, interval=500)
#plt.show()

