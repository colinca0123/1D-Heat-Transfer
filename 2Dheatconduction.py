import numpy as np
import matplotlib.pyplot as plt
#Problem: Continous 1D metal rod
#Rod has certain characteristics: Heat diffusivity constant and its length
#alpha is our heat diffusivity: Lets assume material is copper


a = 110#thermal diffusivity of copper in mm^2/s
length = 50 #50mm
time = 4 #seconds
nodes = 40 #meshes or positions along the rod

#since we are doing a 2D heat transfer a PDE consists of three values that it consists of delta X, y and delta t
#dx and dy represents the space between each node 
#smaller dx the better the precision

dx = length / (nodes-1) #h values
dy = length / (nodes-1)

dt = min(   dx**2 / (4 * a),     dy**2 / (4 * a)) #explicit finite difference method, this makes sure that the simulation does not blow up

t_nodes = int(time/dt) + 1

u = np.zeros((nodes, nodes)) + 20 # Plate is initially as 20 degres C
#initial time distribution at time=0
#initial rod starts at 20 degrees celsius everywhere except the BC
#1D array with 20 elements
#Boundary conditions
u[0, :] = np.linspace(0, 100, nodes)
u[-1, :] = np.linspace(0, 100, nodes)

u[:, 0] = np.linspace(0, 100, nodes)
u[:, -1] = np.linspace(0, 100, nodes)

# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)

# Simulating

counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):
        for j in range(1, nodes - 1):

            dd_ux = (w[i-1, j] - 2*w[i, j] + w[i+1, j])/dx**2
            dd_uy = (w[i, j-1] - 2*w[i, j] + w[i, j+1])/dy**2

            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    counter += dt

    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot

    pcm.set_array(u)
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)


plt.show()




