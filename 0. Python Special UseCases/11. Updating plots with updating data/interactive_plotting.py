import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-10, 11, 1)
y = x**3 + 3*x**2 - 12

# Replace with the path I want to monitor, in this case, it is the current working directory
plt.switch_backend('Qt5Agg')
plt.ion()


#fig, ax = plt.subplots(figsize=(15, 8), dpi=120)

# #ax.clear()
# plt.plot(x, y)
    

# FORCE GUI REFRESH
# fig.canvas.draw_idle()
# fig.canvas.flush_events()    

def plotting_program():
    fig, ax = plt.subplots()
    ax.clear()
    y = x**3 + 3*x**2 - 12
    ax.plot(x, y)
    
    # FORCE GUI REFRESH
    fig.canvas.draw_idle()
    fig.canvas.flush_events() 
    
    
#plotting_program()    