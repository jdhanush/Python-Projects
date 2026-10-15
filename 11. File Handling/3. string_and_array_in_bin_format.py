import pickle
import numpy as np


# Sample data
metadata_string = "Project Run #12"
matrix_data = np.array([[10, 20], [30, 40]])


# Bundle them into a dictionary or tuple and save
data_bundle = {"meta": metadata_string, "matrix": matrix_data}


with open("output.bin", "wb") as f:
    pickle.dump(data_bundle, f)