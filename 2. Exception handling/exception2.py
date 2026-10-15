# this is very generic exception and error handling block.
# the 'except' will catch all the errors so it
print('\n') 
#####################################################################
print('0.1 Basic Error Handling Block')
try:
    print(x)
except:
    print("This is a very generic way of catching an error without identifying the cause/type of error")



    


print('\n')
# this block specifically catches the 'NameError'
#####################################################################
print('0.2 Specific Error Handling Block')
try:
    print(x)
except NameError:
    print("\nThis line is printed because there is a NameError and it is identified")    

    

   

    
print('\n') 
# Selecting the appropriate error type
#####################################################################
x=2
print('1st Error Handling Block where the type of error is known')
try:
    y = x/0
# when there is an error, the appropriate type of exception block is executed
# in this scenario, the NameError is not applicable ZeroDivisionError is applicable   
except NameError:
    print("This line will be skipped if there is no NameError")    
except ZeroDivisionError:
    print('Please do not divide by zero')

    




print('\n') 
# By passing the error messages when there is no error by executing the 'else:' section   
#####################################################################
print('2nd Error Handling Block is when there are no errors')
try:
    z = x/1
# in this scenario, no error is found in the try: section, in that case, the else: section is executed
except NameError:
    print("\nSome of variable(s) may be undefined")    
except ZeroDivisionError:
    print('Please do not divide by zero')
else:
    print("No errors! So this line will be printed")



    


print('\n') 
# Executing the 'finally:' block in the error scenario
#####################################################################
print('3.1rd Error Handling Blockn with finally: section with error')
try:
    y = x/0
# when there is an error, the appropriate type of exception block is executed
# in this scenario, the NameError is not applicable ZeroDivisionError is applicable   
except NameError:
    print("\nSome of variable(s) may be undefined")    
except ZeroDivisionError:
    print('Please do not divide by zero')    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")



       

print('\n') 
# Executing the 'finally:' block in the error-free scenario
#####################################################################
print('3.2rd Error Handling Block with finally: section without error')
try:
    z = x/1
# in this scenario, the NameError is not applicable    
except NameError:
    print("\nSome of variable(s) may be undefined")    
except ZeroDivisionError:
    print('Please do not divide by zero')
else:
    print("No errors!")    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")
    
    
    