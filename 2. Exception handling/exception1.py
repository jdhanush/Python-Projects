print(x)    



# this is very generic exception and error handling block.
# the 'except:' will catch any type of error. Any error in the "try:" then code in 'except:' will be executed
try:
    print(x)
except:
    print("\nThere's an error")
    


# In the first line, we saw that there is a NameError because 'x' is not defined
# Below block specifically catches the 'NameError'
try:
    print(x)
except NameError:
    print("\nThis line is printed because there is a NameError and it is identified")    
    
