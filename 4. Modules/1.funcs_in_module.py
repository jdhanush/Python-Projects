import numpy as np

np_list = []
for item in dir(np):
    np_list.append(item)
    
print(f"The no. of functions in numpy module are: {len(np_list)}")    