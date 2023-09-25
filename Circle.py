from Shapes import Shape
class Circle(Shape):
    def __init__(self , c):
        self.s_area = 0.0
        self.pi = 3.14
        self.c = c


    def __str__(self) -> str:
        return ('Circle Area of '+ str(self.c) + 'C' + str(self.area()))
    def area(self):
        self.s_area = self.pi * (self.c * self.c)
        return self.s_area

cr2 = Circle(10)
print(cr2)
print(cr2.area())



#%%

#%%
