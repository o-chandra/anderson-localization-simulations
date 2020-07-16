import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
import random
from matplotlib import cm

fig = plt.figure()
ax = fig.gca(projection='3d')

#set up the mesh
type=str(input('use test parameters? (yes/no)'))
if type=='no':
    m=int(input('enter number of grid points: '))
    n=int(input('enter potential resolution: '))
    a=float(input('enter lower limit of domain: '))
    b=float(input('enter upper limit of domain: '))
    vmax=int(input('enter maximum potential as an integer: '))
else:
    n=10
    m=5
    a=0
    b=1
    vmax=50

xf=b-a
dx=xf/(n+1)
x = np.linspace(0,xf,n)
y = x
[x,y]=np.meshgrid(x,y)


#set up figure and axes
fig = plt.figure()
ax = fig.gca(projection='3d')

#generate analytic potential
U=np.random.rand(m,m);
print('U is:')
print(U)
#generate projected discretized potential
Ug = np.zeros(x.shape)
for i in range (N):
    for j in range(N):
        delx = float(L)/N;
        dely = delx

        xmin = (i)*delx
        xmax = (i+1)*delx

        ymin = (j)*dely
        ymax = (j+1)*dely

        vid = (x<=xmax) & (x>=xmin) & (y<=ymax) & (y>=ymin)

        Ug[vid] = U[i,j]
print('The projected potential is:')
print(Ug)

#Solve the problem
#allocate space for the operator matrix
H=np.zeros(shape=(n,n))
#Define constants and potential
p=1
def V(x):
    if v=='constant':
        return 0*x
    if v=='linear':
        return x
    if v=='quadratic':
        return x**2
    else:
        print('Invalid potential! Try again.')
        exit()
potential=V(x)
print(len(potential))

#Define boundary conditions

H[0,0]=2*p+V(x[0])
H[0,1]=-p
H[n-1,n-2]=-p
H[n-1,n-1]=2*p+V(x[n-1])

#Fill in the rest of the matrix
for j in range (1, n):
    H[j-1,j-2]=-p
    H[j-1,j-1]=2*p+V(x[j-1])
    H[j-1,j]=-p
print(H)
#Solve for the eigenvalues and eigenvectors, sort them from smallest to largest (abs)
val, vec=np.linalg.eig(H)
z=np.argsort(val)
z=z[0:e]
print(z)
#normalize
energies=(val[z]/val[z][0])
print('the number of selected eigenvalues is:')
print(len(z))
print('The energies are:')
print(energies)

#plot the potential
#define width, depth, height (top and bottom)
width = depth = 1
_v=V(xdim,ydim)
top=_v.ravel()
bottom = np.zeros_like(top)

cmap = cm.get_cmap('Spectral') # Get desired colormap
max_height = np.max(top)   # get range of colorbars so we can normalize
min_height = np.min(top)
# scale each z to [0,1], and get their rgb values
rgba = [cmap((k-min_height)/max_height) for k in top]

ax.bar3d(x,y,bottom,width,depth,top, color=rgba)
plt.show()



#Plot the eigenfunctions and the potential
plt.figure(figsize=(10,10))
for i in range(len(z)):
    y=[]
    y=np.append(y,vec[:,z[i]])
    print ('eigenvector number:')
    print(i+1)
    print(y)
    plt.plot(x,y,lw=3,label="{} ".format(i))
    plt.plot(x,potential, label='{}'.format(i))
    plt.xlabel('x', size=14)
    plt.xlim([0, 1])
    plt.ylabel('$\psi$(x)', size=14)
plt.legend()
plt.title('Normalized eigenfunctions',size=14)
plt.show()
