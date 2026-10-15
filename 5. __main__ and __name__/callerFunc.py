# Importing the file 'funcLib.py' as a module
import funcLib as fL

# Creating an object of 'Wishes' class defined in the 'funcLib' module
obj_1 = fL.Wishes(name = 'Liace')

# Accessing 'greetings()' and 'sendoff()' functions defined in the class 'Wishes' which is inside 'funcLib' user-defined module   
obj_1.greetings()
obj_1.sendoff()
obj_1.nameprinter()