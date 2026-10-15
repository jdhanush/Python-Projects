# defining the class
class Wishes:
    def __init__(self, name):
        self.name = name
    
    # defining the functions which operate on the attributes defined in the constructor '__init__()' function
    def greetings(self):
        print(f"Hi {self.name}")

    def sendoff(self):
        print(f"Bye {self.name}")
        
    def nameprinter(self):
        print(__name__)
        
    


    
if __name__ == "__main__" : 
    print("This line prints only when 'funcLib.py' (this file) is run. \
          \nNOT when this file is imported as 'funcLib' module by another program")
   


#print("\nThis line is a part of the file/module and prints even without specifically calling it.")   
print("\nThis line prints irrespective of direct execution of 'funcLib.py' (this file) OR \
      \nWhen this file is imported as a 'funcLib' module by another program\n")
    