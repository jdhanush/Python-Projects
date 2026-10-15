# class A:
#     x = 7
    
    
# class B:
#     A_obj = A() 
#     l = A_obj.x
#     # def start():
#     #     A_obj = A() 
#     #     print(A_obj.x)
        
# B_obj = B()
# print(B_obj.l)
# #.start()        

#################################
# Why this works?
class A:
    def Aa(self):
        self.x = 7
        return self.x
        
class B:
    def Bb(self):
        A_obj = A() 
        l = A_obj.Aa() 
        print(l)
        
B_obj = B()
B_obj.Bb()
        



#################################
# Why this doesn't work?
class A:
    def Aa(self):
        x = 7
        return x
        
class B:
    def Bb(self):
        A_obj = A() 
        l = A_obj.Aa() 
        print(l.x)
        
B_obj = B()
B_obj.Bb()