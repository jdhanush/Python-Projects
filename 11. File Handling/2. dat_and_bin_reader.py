"""
This program reads .dat and .bin files
"""

import os
import numpy as np

current_working_directory = os.getcwd()

# assigning paths
bin_filepath = os.path.join(current_working_directory, "written_data.bin")
dat_filepath = os.path.join(current_working_directory, "written_data.dat")


# reading .bin file
with open(bin_filepath, "rb") as file:
    bin_data = np.fromfile(file, dtype=np.float64)

    
# reading .dat file    
with open(dat_filepath, "r") as file:
    dat_data = file.readlines()