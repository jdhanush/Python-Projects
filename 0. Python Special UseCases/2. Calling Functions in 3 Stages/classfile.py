import matplotlib.pyplot as plt
# import glob
# import sys
# import os
# import numpy.random as rd
import numpy as np


class DataExtractorClass:
    
    def __init__(self, filepath):
        #self.filepath = filepath
        
        start_of_data_line_no = 13
        start_of_data_line_no -= 1
        
        with open(filepath, 'r') as f:
            self.bulk_lines = f.readlines() 
        
        data_lines = [line for line in self.bulk_lines[start_of_data_line_no:] if line.strip()]

        # Convert to the list to floating point array
        self.data_raw_matrix = np.array([list(map(float, line.split())) for line in data_lines ])
        
        self.firstline = self.data_raw_matrix[0]
        self.secondline = self.data_raw_matrix[1]



class PlottingClass:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def plotfunc(self):
        plt.plot(self.x, self.y)
        

# x = np.linspace(1, 10, 100)
# y = np.linspace(-10, -1, 100)

# if __name__ == "__main__":
#     A = PlottingClass(x, y)
#     A.plotfunc()
    
        