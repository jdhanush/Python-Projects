class AddSub:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def add(self):
        c = self.a + self.b
        return c
    
    def sub(self):
        d = self.a - self.b
        return d

    


class MultDiv:
    def __init__(self, e, f):
        self.e = e
        self.f = f
        
    def aplusbs(self):
        obj = AddSub(self.e, self.f)
        return obj.add()
    
    def aminusbs(self):
        obj = AddSub(self.e, self.f)
        return obj.sub()


print("\nPrinting class AddSub")
int_obj = AddSub(2,3)
print(int_obj.add())
print(int_obj.sub())


print("\nPrinting class MultDiv")
ext_obj = MultDiv(5,6)
print(ext_obj.aplusbs())
print(ext_obj.aminusbs())