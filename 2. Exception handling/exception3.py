# Not just catching the error, we have to know what is the type of the error
x = 2


#####################################################################
print("Block 1")
try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed, ji")

except TypeError:
    print("The defined variable is not a string datatype")  

except Exception as error:
    print(error)
    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")
    


print('\n')    
#####################################################################
print("Block 2")
try:
    if not type(x) is str:
        raise TypeError("Only strings are allowed, ji")
      
except Exception as error:
    print(error)    
    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")
    


print('\n')
#####################################################################
print("Block 3")
try:
    if not type(x) is str:
        raise Exception("I'm a custom exception")

except TypeError:
    print("The defined variable is not a string datatype")  

except Exception as error:
    print(error)    
    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")
    
    

print('\n')    
#####################################################################
print("Block 4")
try:
    if not type(x) is str:
        raise Exception("I'm a custom exception")
      
except Exception as error:
    print(error)     

finally:
    print("I'm going to print this line irrespective of whether there is error or not")
    
    
    
    
    
    
    
    
    
    
    