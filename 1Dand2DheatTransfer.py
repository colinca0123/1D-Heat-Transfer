import numpy as np
import matplotlib.pyplot as plt
#Problem: Continous 1D metal rod
#Rod has certain characteristics: Heat diffusivity constant and its length
#alpha is our heat diffusivity: Lets assume material is copper

a=110 #thermal diffusivity of copper in mm^2/s
length=50 #50mm
time=4 #seconds
nodes=50 #positions along the rod

#since we are doing a 1D heat transfer a PDE consists of two values that it consists of delta X and delta t
#dx represents the space between each node 
#smaller dx the better the precision

#Initialization

dx=length/(nodes) #h value
dt=0.5*dx**2/a #explicit finite difference method, this makes sure that the simulation does not blow up
t_nodes=int(time/dt) #number of loops for each simulation



T=np.zeros(nodes)+20 #initial time distribution at time=0
#initial rod starts at 20 degrees celsius everywhere except the BC
#1D array with 20 elements
#Boundary conditions
T[0]=100
T[-1]=100


#visualize

fig, axis= plt.subplots() #creates a figure and a set of axes 
pcm=axis.pcolormesh([T], cmap='jet', vmin=0, vmax=100) #vmin is 0 which corresponds to blue and 100 corresponds to red, this turns the data into a heat map
#pcolormesh makes a psuedocolor plot
#need a 2D array because need to make a grid of rectangles
#in this case it has a rectangular grid of 1 row and 20 columns
plt.colorbar(pcm, ax=axis) #color legend

axis.set_xlabel('Position along rod (mm)')
axis.set_ylabel('Time(s)')
axis.set_ylim([-2,3])






#simulation
counter=0

while counter<time: #loops run until counter reaches 4 seconds
    w=T.copy()
    
    for i in range(1, nodes-1): #the boundary condition are satisfied at the nodes at index 0 and 9
        T[i]=dt*a*(w[i+1]-2*w[i]+w[i-1])/dx**2+w[i] #this is the taylor series differential for the 1D heat equation
    counter+=dt
    print('Temp at', counter, '[s]', 'Average Temperature:', np.average(T), 'Celsius' )
    axis.set_title("Distribution at t: {:.3f} [s]".format(counter))
    #updating the plot
    pcm.set_array([T]) #this updates the color to match the pcm colormesh
    plt.pause(0.01)



plt.show()