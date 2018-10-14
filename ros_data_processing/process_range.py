import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd

#sns.set()
#sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}

# matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
plt.style.use('fivethirtyeight')


range_luke = pd.read_csv('initial_test_oct4/range_luke.csv')
range_jer = pd.read_csv('initial_test_oct4/range_jer.csv')

print('Luke: {:.3f} +/- {:.3f} m'.format(range_luke.dist.mean(), range_luke.dist.std()))
print('Jer: {:.3f} +/- {:.3f} m'.format(range_jer.dist.mean(), range_jer.dist.std()))

range_luke.rosbagTimestamp -= range_luke.rosbagTimestamp.min()
range_luke.rosbagTimestamp *= 30e-11

plt.figure(figsize=(8, 8))
plt.plot(range_luke.rosbagTimestamp, range_luke.dist, marker='.', linestyle='None', markersize=10)
plt.fill_between(range_luke.rosbagTimestamp, ((range_luke.rosbagTimestamp * 0) + 1) * (3.797 + .04), ((range_luke.rosbagTimestamp * 0) + 1) * (3.797 - .04), alpha=.3, color='g')
plt.legend(['Range data', '$\mu \pm 1\sigma$'])
plt.xlabel('Time [ seconds ]')
plt.ylabel('Range [ m ]')
plt.tight_layout()
plt.savefig('range.png')
plt.show()
