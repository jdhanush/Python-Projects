import numpy as np

a1 = np.arange(0, 10)
b1 = np.arange(10, 20)
c1 = np.arange(20, 30)
d1 = np.arange(30, 40)
e1 = np.arange(50, 60)
f1 = np.arange(60, 70)

A = a1
var_dict = {0:a1, 1:b1, 2:c1, 3:d1, 4:e1, 5:f1,}

for i in range(1,6):
    A = np.column_stack((A, var_dict[i]))
    print(f"Updated matrix: \n{A} \n{A.shape} \n")


print(f"Fully updated matrix {A} \n{A.shape}")