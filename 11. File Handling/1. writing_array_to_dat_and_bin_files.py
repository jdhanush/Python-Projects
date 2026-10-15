"""
This program writes the numpy array data to .dat and .bin files
"""


import os
import numpy as np

current_working_directory = os.getcwd()

# Sample data
arr_data = np.array([[1.5, 2.3, 3.1], [4.0, 5.2, 6.8]])

dat_filepath_write = os.path.join(current_working_directory, "written_data.dat")
bin_filepath_write = os.path.join(current_working_directory, "written_data.bin")

#np.savetxt(filepath_write, data, delimiter=' ', fmt='%.2f)     # this allows us to store the numbers in 2 decimal places      
np.savetxt(dat_filepath_write, arr_data, delimiter=' ')
print("file written in .dat format")

arr_data.tofile(bin_filepath_write)
print("file written in .bin format")  

print(f"""\nNote that the data format of each element of arr_data is {type(arr_data[0][0])}. 
Therefore, we have to read the data file in the same data format""")