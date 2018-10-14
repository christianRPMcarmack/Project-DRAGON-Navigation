import matplotlib.pyplot as plt
import numpy as np
from math import *
import seaborn as sns
import pandas as pd
import ast
import scipy.integrate
from mpl_toolkits.mplot3d import Axes3D


#sns.set()
#sns.set_context('poster')

font = {'family' : 'serif',
        'weight' : 'bold',
        'size'   : 16}


# matplotlib.rc('font', **font)
plt.rc('text', usetex=True)
plt.style.use('fivethirtyeight')

imu_df = pd.read_csv('initial_test_oct4/imu.csv')

# Remove empty columns
imu_df.dropna(axis='columns', thresh=1000, inplace=True)

# Better time, relative to start
imu_df['imu_time'] = imu_df.secs + imu_df.nsecs * 1e-9 
imu_df.imu_time -= imu_df.imu_time.min()

# Covariance matrices only have diag(value) 3x3
angular_velocity_covariance = ast.literal_eval(imu_df.angular_velocity_covariance.iloc[0])[0]
linear_acceleration_covariance = ast.literal_eval(imu_df.linear_acceleration_covariance.iloc[0])[0]

# Remove columns we don't need
imu_df.drop(['seq', 'frame_id', 'orientation_covariance', 'secs', 'nsecs', 'angular_velocity_covariance', 'linear_acceleration_covariance'], axis=1, inplace=True)

imu_df.rename(index=str, columns={"x": "orient_imu_x", "y": "orient_imu_y", "z": "orient_imu_z", "w": "orient_imu_w",
                                  "x.1": "omega_imu_x", "y.1": "omega_imu_y", "z.1": "omega_imu_z",
                                  "x.2": "alpha_imu_x", "y.2": "alpha_imu_y", "z.2": "alpha_imu_z",},
                                  inplace=True)
                                  
imu_df.set_index('rosbagTimestamp', inplace=True)

def accel_to_pose(time, accel):
    return .5 * np.insert(scipy.integrate.cumtrapz(np.insert(scipy.integrate.cumtrapz(accel, time), 0, 0., axis=0), time), 0, 0., axis=0)

def accel_to_vel(time, accel):
    return np.insert(scipy.integrate.cumtrapz(accel, time), 0, 0., axis=0)
    
imu_df.alpha_imu_x -= imu_df.alpha_imu_x.mean()
imu_df.alpha_imu_y -= imu_df.alpha_imu_y.mean()
imu_df.alpha_imu_z -= imu_df.alpha_imu_z.mean()

imu_df['integrated_vx'] = accel_to_vel(imu_df.imu_time.values, imu_df.alpha_imu_x.values)    
imu_df['integrated_x'] = accel_to_pose(imu_df.imu_time.values, imu_df.alpha_imu_x.values)

imu_df['integrated_vy'] = accel_to_vel(imu_df.imu_time.values, imu_df.alpha_imu_y.values)    
imu_df['integrated_y'] = accel_to_pose(imu_df.imu_time.values, imu_df.alpha_imu_y.values)

imu_df['integrated_vz'] = accel_to_vel(imu_df.imu_time.values, imu_df.alpha_imu_z.values)    
imu_df['integrated_z'] = accel_to_pose(imu_df.imu_time.values, imu_df.alpha_imu_z.values)
 
plt.figure(figsize=(8, 8))
plt.plot(imu_df.imu_time, imu_df.integrated_x, label='$x$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.integrated_vx, label='$v_x$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.alpha_imu_x, label='$a_x$', marker='.', linestyle='None')
plt.title('IMU $x$ Integration')
plt.xlabel('Time [ seconds ]')
plt.ylabel('m, m/s, m/s$^2$')
plt.legend()
plt.tight_layout()
plt.savefig('x_imu.png')
plt.close()

plt.figure(figsize=(8, 8))
plt.plot(imu_df.imu_time, imu_df.integrated_y, label='$y$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.integrated_vy, label='$v_y$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.alpha_imu_y, label='$a_y$', marker='.', linestyle='None')
plt.title('IMU $y$ Integration')
plt.xlabel('Time [ seconds ]')
plt.ylabel('m, m/s, m/s$^2$')
plt.legend()
plt.tight_layout()
plt.savefig('y_imu.png')
plt.close()

plt.figure(figsize=(8, 8))
plt.plot(imu_df.imu_time, imu_df.integrated_z, label='$z$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.integrated_vz, label='$v_z$', marker='.', linestyle='None')
plt.plot(imu_df.imu_time, imu_df.alpha_imu_z, label='$a_z$', marker='.', linestyle='None')
plt.title('IMU $z$ Integration')
plt.xlabel('Time [ seconds ]')
plt.ylabel('m, m/s, m/s$^2$')
plt.legend()
plt.tight_layout()
plt.savefig('z_imu.png')
plt.close()

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.plot(imu_df.integrated_x, imu_df.integrated_y, imu_df.integrated_z)
#plt.show()




tars_df = pd.read_csv('initial_test_oct4/tars.csv')

# Remove empty columns
tars_df.dropna(axis='columns', thresh=1000, inplace=True)

# Better time, relative to start
tars_df['tars_time'] = tars_df.secs + tars_df.nsecs * 1e-9 

tars_df.rename(index=str, columns={"x.1": "rot_x", "y.1": "rot_y", "z.1": "rot_z", "w": "rot_w",},
                                  inplace=True)

# Remove columns we don't need
tars_df.drop(['seq', 'frame_id', 'child_frame_id','secs', 'nsecs'], axis=1, inplace=True)

tars_df.x -= tars_df.x[0]
tars_df.y -= tars_df.y[0]

tars_df.set_index('rosbagTimestamp', inplace=True)





rover_df = imu_df.join(tars_df, how='outer')

# cubic poly sucks-- doesn't capture peaks
rover_df = rover_df.apply(pd.Series.interpolate, args=('linear',))
rover_df.dropna(inplace=True)

# Reindex to real time
rover_df.rename(index=str, columns={'imu_time': 'time'})
rover_df.set_index('imu_time', inplace=True)


# Work with first 10 seconds for now
rover_df = rover_df.loc[0:50]

def q_mult(q1, q2):
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    w = w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2
    x = w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2
    y = w1 * y2 + y1 * w2 + z1 * x2 - x1 * z2
    z = w1 * z2 + z1 * w2 + x1 * y2 - y1 * x2
    return w, x, y, z

def q_conjugate(q):
    w, x, y, z = q
    return (w, -x, -y, -z)

def quat_rotation(x_list, y_list, z_list, qx_list, qy_list, qz_list, qw_list):
    rot_x = []
    rot_y = []
    rot_z = []
    
    for x, y, z, qx, qy, qz, qw in zip(x_list, y_list, z_list, qx_list, qy_list, qz_list, qw_list):
        q = np.array([qw, qx, qy, qz])
        v = np.array([0., x, y, z])
        
        v_p = q_mult(q_mult(q, v), q_conjugate(q))[1:]
        
        rot_x.append(v_p[0])
        rot_y.append(v_p[1])
        rot_z.append(v_p[2])
    
    return rot_x, rot_y, rot_z
    
rotated_vector = quat_rotation(rover_df.integrated_x.values, rover_df.integrated_y.values, rover_df.integrated_z.values, 
                           rover_df.rot_x.values, rover_df.rot_y.values, rover_df.rot_z.values, rover_df.rot_w.values)
                           
rover_df['xp'] = rotated_vector[0]
rover_df['yp'] = rotated_vector[1]
rover_df['zp'] = rotated_vector[2]

fig, ax = plt.subplots()
ax.plot(rover_df.integrated_x, rover_df.integrated_y, label='IMU')
ax.plot(rover_df.xp, rover_df.yp, label='IMU Rot')
ax.plot(rover_df.x, rover_df.y, label='TARS')
ax.legend()
plt.show()

