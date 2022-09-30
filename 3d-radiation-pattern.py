#Defining given conditions
freq = 2.4*10**9 # frequency in Hertz
lambdaa = 3*10**8/freq

#Define length of current element in terms of lambda
l=2*lambdaa


# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d

# Sampling values of theta and phi in respective range: theta(-pi, pi), phi(0, 2pi)
phi, theta = np.linspace(0, 2 * np.pi, 100), np.linspace(-np.pi, np.pi, 100)
PHI, THETA = np.meshgrid(phi, theta) # converting arrays to 2-D grid

# Using the function which defines E-plane radiation pattern
R = (np.cos(2*np.pi/lambdaa*l/2*np.cos(THETA)) - np.cos(2*np.pi/lambdaa*l/2))/np.sin(THETA)

# Converting to cartesian coordinates
X = R * np.sin(THETA) * np.cos(PHI)
Y = R * np.sin(THETA) * np.sin(PHI)
Z = R * np.cos(THETA)

# Plotting the radiation pattern
fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(1,1,1, projection='3d')
plot = ax.plot_surface(
    X, Y, Z, rstride=1, cstride=100,color='green',
    linewidth=0.2, antialiased=False, alpha=0.1, edgecolor='green')
plt.show()