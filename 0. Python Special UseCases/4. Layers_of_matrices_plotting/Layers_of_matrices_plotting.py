import numpy as np
import matplotlib.pyplot as plt

y0 = np.array([[1, 2], [3, 4]])
y1 = np.array([[5, 6], [7, 8]])
y2 = np.array([[ 9, 10], [11, 12]])

lay = [y0, y1, y2]

no_of_files = len(lay)
fig, axs = plt.subplots(1, no_of_files, sharex=True, figsize=(30, 10))
fig.suptitle("Range–Doppler Plot\n ", fontsize=18, fontweight='bold', c='blue')

for ax, data in zip(axs, lay):    
    ax.scatter(data[0], data[1], color='r', linewidth=2) 
    ax.plot(data[0], data[1], color='k', linewidth=1) 
    ax.set_xlabel("Doppler (Hz)")
    print(f'{data}\n')
    


# def matrix_Book_Plotter(lay):
#     fig, axs = plt.subplots(1, no_of_files, sharex=True, figsize=(30, 10))
#     fig.suptitle("Range–Doppler Plot\n ", fontsize=18, fontweight='bold', c='blue')

#     for ax, data in zip(axs, lay):    
#         ax.plot(data[0], data[1], color='k', linewidth=1) 
#         ax.set_xlabel("Doppler (Hz)")
#         print(data)   
