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
        print(f"\nI'm {self.make} {self.model} car")
 
        
 
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




# From here we'll implement the Inheritance below

# In general, an airplane will have 'FAA_ID'(an additional attribute) apart from the 'make' and 'model' attributes 
# Therefore, we will define new variable faa_id
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)   # this one line would replace "self.make = make" and "self.model = model" variable assignment lines
        self.faa_id = faa_id
        
    def moves(self):
        print("Airplane flies along")
        
    def get_faa(self):
        print(f"The FAA of this {self.make} {self.model} is: {self.faa_id}")
        
        
class Truck(Vehicle):
    def moves(self):
        print("Truck rumbles along")        
        
class GolfCart(Vehicle):
    pass


# creating Objects correspoding to the 'Airplane', 'Truck' and 'GolfCart' classes

# Assigning the FAA_ID in this Airplane  
cessna = Airplane("Cessna", "Skyhawk", "N-123")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")


# Applying the methods and accessing the variables from the object 'cessna' 
# the moves() function defined inside the child class 'Airplane' overwrites the move() method defined in its parent class 'Vehicle'         
cessna.get_make_model()
cessna.moves()
cessna.get_faa()

# Applying the methods and accessing the variables from the object 'mack'        
# the moves() function defined inside the child class 'Truck' overwrites the move() method defined in its parent class 'Vehicle'         
mack.get_make_model()
mack.moves()

# Applying the methods and accessing the variables from the object 'golfwagon' 
# Please note we didn't define any specific moves() method in the 'GolfCart' class. 
# Therefore, when moves() method is called in the 'golfwagon' object, it uses the method from the parent class 'Vehicle'         
golfwagon.get_make_model()
golfwagon.moves()        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        