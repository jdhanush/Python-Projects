class Vehicle:
    
    # The attributes (properties, characteristics, or states) of the class can be defined in the initializer function '__init__()'
    # the properties are passed into __init__() function while all other 'def' s are methods
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def moves(self):
        print("Car Moves Along ...")
    
    # this is a getter function which can fetch all the variables at the same time    
    def get_make_model(self):
        print(f"I'm {self.make} {self.model} car")
 
        
 
# 'my_car' is an object that is created from the class 'Vehicle'
# and two parameters are passed         
my_car = Vehicle(make='Tesla', model='Model 3')

# The below two print statements are retrieving the variables individually
print(my_car.make)
print(my_car.model)

# Accessing the varibles using the getter function
my_car.get_make_model()

# Accessing one of the methods in the Vehicle class
my_car.moves()        


print('\n')
# Below is the 2nd car object with the same 'Vehicle' class
your_car = Vehicle("Cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


# IN summary, 'Vehicle' is the class, 'my_car' and 'your_car' are the objects of the class