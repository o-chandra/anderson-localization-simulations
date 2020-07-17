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

U=np.random.rand(m,m) #generate analytic potential
print ('the analytic potential is:')
print(U)
#generate projected discretized potential
Ug = np.zeros(x.shape)
for i in range (m):
    for j in range(m):
        delx = float(xf)/m;
        dely = delx

        xmin = (i)*delx
        xmax = (i+1)*delx

        ymin = (j)*dely
        ymax = (j+1)*dely

        vid = (x<=xmax) & (x>=xmin) & (y<=ymax) & (y>=ymin)

        Ug[vid] = U[i,j]
print('the discretized potential is:')
print(Ug)
#Solve the problem
#allocate space for the operator matrix
H=np.zeros(shape=(m,m))
#Define constants
p=1
V=Ug
print("V is:")
print(V)
v=V.item((0,0))
print(v)

 ###I don't think this is the right form for the operator matrix in 2d: need to rederive w/ new stencil!###
 #Define boundary conditions
H[0,0]=2*p+V.item(0,0)
H[0,1]=-p
H[m-1,m-2]=-p
H[m-1,m-1]=2*p+V.item((m-1,m-1))

#Fill in the rest of the matrix
for j in range (1, m):
    H[j-1,j-2]=-p
    H[j-1,j-1]=2*p+V.item((j-1,j-1))
    H[j-1,j]=-p
print(H)
#Solve for the eigenvalues and eigenvectors, sort them from smallest to largest (abs)
val, vec=np.linalg.eig(H)
z=np.argsort(val)
z=z[0:vmax]
print(z)

energies=(val[z]/val[z][0]) #normalize
print('the number of selected eigenvalues is:')
print(len(z))
print('The energies are:')
print(energies)

#plot the eigenfunctions and eigenvalues


fig = plt.figure() #set up figure and axes
ax = fig.gca(projection='3d')

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
    plt.ylabel('$\psi$(x)', size=14)
plt.legend()
plt.title('Normalized eigenfunctions',size=14)
plt.show()
