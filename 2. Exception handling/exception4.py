# Creating an exception class
class JustNotCoolError(Exception):
    pass


x = 2
try:
    if not type(x) is str:
        raise JustNotCoolError("This isn't just cool, man")     # calling the custom error
      
except Exception as error:
    print(error)     
    
finally:
    print("I'm going to print this line irrespective of whether there is error or not")    