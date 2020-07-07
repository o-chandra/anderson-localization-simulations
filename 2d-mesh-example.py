import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

#set up grid points
xval=np.array([0,1,2,3])
yval=np.array([0,1,2,3])
x,y=np.meshgrid(xval,yval)
print("x is:")
print(xval)
print("y is:")
print(yval)
print("the x coordinates of the mesh are:")
print(x)
print("the y coordinates of the mesh are:")
print(y)

#for i in range(len(xval)):
#    print(x[0,i])


#define the potential
def V(x,y):

    for i in range(len(xval)):
        if 0<x[0,i]<1:
            return 0
        else:
            return 1
v=V(x,y)
print("the potential is")
print(v)

#plot the mesh and the potential
#plt.plot(x, y, marker='.', color='k', linestyle='none')
#ax.plot_surface(x,y,v,cmap='cool')
#plt.show()
