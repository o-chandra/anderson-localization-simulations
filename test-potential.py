import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot
import random


N=2 #analytic potential size
Ng=4 #grid points

#generate analytic potential
U=np.random.rand(N,N);
print('U is:')
print(U)
#define parameters
L=1 #domain length (b-a)
x = np.linspace(0,L,Ng)
y = x
[x,y]=np.meshgrid(x,y)
Ug = np.zeros(x.shape)

#define projected potential
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
print('Ug is:')
print(Ug)
