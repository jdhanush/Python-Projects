import matplotlib.pyplot as plt
import numpy as np


X = [2, 7, 10]
Y = [1, 4, 9]


intensity_list = ['Low', 'Med', 'High']

# Individual Linear Plotting case
#################################################################
fig1, ax1 = plt.subplots()
ax1.plot(X, Y)

#####
# here the ticks ['Low', 'Med', 'High'] map to values in 'X'
#####
ax1.set_xticks(X)
ax1.set_xticklabels(['Low', 'Med', 'High'])







# Color map Plotting case
#################################################################
A, B = np.meshgrid(X, Y)
global_min = np.min(A)
global_max = np.max(A)

fig2, ax2 = plt.subplots()

#####
# here the ticks ['Low', 'Med', 'High'] map to [0, 1, 2,...]
#####
ax2.set_xticks(np.arange(len(X)))
ax2.set_xticklabels(intensity_list)


im = ax2.pcolormesh(A, cmap="jet", vmin=np.min(A), vmax=np.max(A), shading= 'gouraud' if A.shape[1] > 1 else 'auto')
cbar = fig2.colorbar(im, ax=ax2, fraction=0.05, pad=0.05)
cbar.ax.tick_params(labelsize=4)

