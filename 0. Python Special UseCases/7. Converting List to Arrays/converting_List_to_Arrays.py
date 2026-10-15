import numpy as np

u0 = np.array([0, 2, 4, 6, 8])
v0 = np.array([1, 3, 5, 7, 9])
ws0 = np.round(np.sqrt(u0**2 + v0**2), 2)

u1 = np.array([10, 12, 14, 16, 18])
v1 = np.array([21, 23, 25, 27, 29])
ws1 = np.round(np.sqrt(u1**2 + v1**2), 2)

print(f"\nws0 = {ws0}, shape = {ws0.shape}\n and \nws1 = {ws1}, shape = {ws1.shape}\n")

u_list = []
v_list = []

u_list.append(u0)
u_list.append(u1)

v_list.append(v0)
v_list.append(v1)

u_mat = np.array(u_list)
v_mat = np.array(v_list)

print(f"\nWithout transpose u_mat: \n{u_mat} \nshape is {u_mat.shape}")
print(f"\nWithout transpose v_mat: \n{v_mat} \nshape is {v_mat.shape}\n")

u_mat_trans = np.array(u_list).T
v_mat_trans = np.array(v_list).T

print(f"\nWithout transpose u_mat_trans: \n{u_mat_trans} \nshape is {u_mat_trans.shape}")
print(f"\nWithout transpose v_mat_trans: \n{v_mat_trans} \nshape is {v_mat_trans.shape}\n")