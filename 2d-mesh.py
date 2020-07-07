import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')
#two dimensional mesh for solving the Schrodinger equation using finite differences on a square domain

#enter mesh parameters
type=str(input('use test parameters? (yes/no)'))
if type=='no':
    n=int(input('enter number of grid points: '))
    a=float(input('enter lower limit of domain: '))
    b=float(input('enter upper limit of domain: '))
else:
    n=10
    a=0
    b=1

xval=np.linspace(b,a, n)
print(xval)
first=xval[0]
print(first)
second=xval[1]
print(second)
yval=np.linspace(b,a,n)
x,y=np.meshgrid(xval,yval)
print(x,y)
#change this definition
def V(x,y):
     return np.piecewise(x, [x==y, x!=y], [1,0])
v=V(x,y)
#plot the grid
plt.plot(x, y, marker='.', color='k', linestyle='none')
#plot the potential
ax.plot_surface(x,y,v,cmap='cool')
plt.show()
