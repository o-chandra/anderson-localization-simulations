import numpy as np
import matplotlib.pyplot as plt


n=10  #number of grid points
P=10 # period
D=5 #grid spacing

potential=np.arange(n) % P < D
print("the potential is")
print(potential)

#plot the mesh and the potential
plt.plot(potential)
plt.ylim(-0.5, 1.5)
plt.show()
