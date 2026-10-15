# This code lists all the plotting styles available
from matplotlib import pyplot as plt

plotting_styles = plt.style.available

for style in plotting_styles:
    print(style)