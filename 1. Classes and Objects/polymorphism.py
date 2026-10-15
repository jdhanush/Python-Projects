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
        print(f"\nI'm {self.make} {self.model}")
 
        
 

###################################################################################################################
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


# creating 'my_car', 'your_car' objects using 'Vehicle' class
my_car = Vehicle(make='Tesla', model='Model 3')
your_car = Vehicle("Cadillac", "Escalade")

# creating Objects correspoding to the 'Airplane', 'Truck' and 'GolfCart' classes
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaha", "GC100")
# Assigning the FAA_ID in this Airplane  
cessna = Airplane("Cessna", "Skyhawk", "N-123")


   
             

###################################################################################################################
# From here we'll implement the Polymorphism below         
print('\n')
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()
    v.moves()
# In this for loop, the same methods get_make_model() and moves() will give different output for different objects
# The output is dependent upon the method that is either inherited from the parent class or defined within its own class        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        