'''
This program is for getting the iteration number,
at the same time to access the data inside the list index by index.
'''

import numpy as np
x = np.array([1,2,23,5,7])
beam_start_time_list = ['17:13:6', '17:13:23', '17:13:39', '17:13:57', '17:14:12']    
filename_list = ['SpectralData1', 'SpectralData2', 'SpectralData3', 'SpectralData4', 'SpectralData5']

# The last argument 'start = 1' inside the enumerate() lets the loop start throw the iteration value = 1
for iteration, (x_val, beam_timestamp, filename) in enumerate(zip(x, beam_start_time_list, filename_list), start = 1):
    print(f'For iteration: {iteration}, beam_timestamp = {beam_timestamp}, filename = {filename}')
    
    