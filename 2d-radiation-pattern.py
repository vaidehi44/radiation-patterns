#Defining given conditions
freq = 2.4*10**9 # frequency in Hertz
lambdaa = 3*10**8/freq

#Define length of current element in terms of lambda
l=2*lambdaa


# Importing required libraries
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d


# Defining phi and theta for phi=0 and theta=(-pi, pi)
phi_1, theta_1 = np.linspace(0, 0, 100), np.linspace(-np.pi, np.pi, 100)
PHI_1, THETA_1 = np.meshgrid(phi_1, theta_1) # converting arrays to 2-D grid

# Using the function which defines E-plane radiation pattern
R_1 = (np.cos(2*np.pi/lambdaa*l/2*np.cos(THETA_1)) - np.cos(2*np.pi/lambdaa*l/2))/np.sin(THETA_1)

# Converting to cartesian coordinates
X_1 = R_1 * np.sin(THETA_1) * np.cos(PHI_1)
Y_1 = R_1 * np.sin(THETA_1) * np.sin(PHI_1)
Z_1 = R_1 * np.cos(THETA_1)


fig = plt.figure(figsize=(12,12))
ax = fig.add_subplot(1,1,1, projection='3d')
ax.view_init(0, 90) # rotating the axes to see the 2D plot

# Plotting the radiation pattern for phi=0
plot1 = ax.plot_surface(
    X_1, Y_1, Z_1, rstride=1, cstride=100,color='green',
    linewidth=0.2, antialiased=False, alpha=0.2, edgecolor='green')

# Defining phi and theta for phi=pi and theta=(-pi. pi)
phi_2, theta_2 = np.linspace(np.pi, np.pi, 100), np.linspace(-np.pi, np.pi, 100)
PHI_2, THETA_2 = np.meshgrid(phi_2, theta_2) # converting arrays to 2-D grid

# Using the function which defines E-plane radiation pattern
R_2 = (np.cos(2*np.pi/lambdaa*l/2*np.cos(THETA_2)) - np.cos(2*np.pi/lambdaa*l/2))/np.sin(THETA_2)

# Converting to cartesian coordinates
X_2 = R_2 * np.sin(THETA_2) * np.cos(PHI_2)
Y_2 = R_2 * np.sin(THETA_2) * np.sin(PHI_2)
Z_2 = R_2 * np.cos(THETA_2)

# Plotting the radiation pattern for phi=pi
plot2 = ax.plot_surface(
    X_2, Y_2, Z_2, rstride=1, cstride=100,color='green',
    linewidth=0.2, antialiased=False, alpha=0.2, edgecolor='green')
plt.show()