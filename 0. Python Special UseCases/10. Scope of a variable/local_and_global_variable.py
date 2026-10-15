
v1 = 0      # Initial assignment of v1 outside function
v2 = 3      # Initializing v2 outside function
# At this stage, v1 and v2 have no difference



def value_printer():
    global v1   # initializing v1 as a global variable
    v1 = 1      # assigning value to v1 different from what was assigned outside function
    v2 = 7      # assigning value to v2 different from what was assigned outside function
    print(f"values Inside function \nv1 = {v1}; v2 = {v2}")
    
    
value_printer()    
print(f"\nvalues Outside function \nv1 = {v1}; v2 = {v2}")