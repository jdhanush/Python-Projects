# parent class
class A:
    def __init__(self, var_A):
        self.a = var_A
#        self.x = x
    
    def getVar(self):
        print(self.a)
    
    rdnum = 67    
        
    def changeVar(self, x):
        self.x  = x+5
        

# child class
class B(A):
    def add(self, c):
        self.b = self.a + c
        print(self.b)
    
    def sqf(self):
        self.y = self.x**2
        #return self.y
        
        

        
# obj_A = A(1)
# obj_A.changeVar(x=10)

obj_B = B(1)
#obj_B.add(3)     
obj_B.changeVar(x=7)
b_x = obj_B.x
obj_B.sqf()
print(f"\ny = {obj_B.y}")
