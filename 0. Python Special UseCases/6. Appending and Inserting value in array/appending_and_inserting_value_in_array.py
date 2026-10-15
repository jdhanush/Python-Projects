import numpy as np
value_to_be_inserted = 0


# Initializing an array
WSp = np.array([1, 7, 22, 10, 15, 18])
print(f"WSp = {WSp}")


# Difference array: higher_index_value - lower_index_value 
WSh = np.diff(WSp)
print(f"WSh = {WSh}")


# appending 'value_to_be_inserted' at the end of the array
WSh_new = np.append(WSh, value_to_be_inserted)
print(f"WSh_new = {WSh_new}")


# inserting 'value_to_be_inserted' at the desired index 
print("\n")
for index in range(len(WSh)):
    WSh_new = np.insert(WSh, index, value_to_be_inserted)
    print(f"\nfor i={index} \nWSh_new = {WSh_new}")
    