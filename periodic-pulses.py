import numpy as np
import matplotlib.pyplot as plt
N = 100 # sample count
P = 10  # period
D = 5   # width of pulse
sig = np.arange(N) % P < D
print(sig)
plt.plot(sig)
plt.ylim(-0.5, 1.5)
plt.show()
