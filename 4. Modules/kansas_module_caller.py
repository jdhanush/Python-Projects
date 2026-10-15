# importing the module
import kansas_Module as k 

# Accessing the variable from the module
print("\n Variables from the 'kansas_Module' module:")
print(k.bird)
print(k.capital)

# Accessing the method from the module
print("\n A random fact from the 'kansas_Module' module:")
k.randomfunfact()

# Dtermining the name of the current file and the module file
print('\n Understanding current and the imported module file access names')
print(__name__)
print(k.__name__)
