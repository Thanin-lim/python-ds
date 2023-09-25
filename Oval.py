import math
from Shapes import Shape
class ovals(Shape):
    def __init__(self,o)-> None:
        self.sqr_oval=0.0
        self.o=o
        self.pi=math.pi
    def area_o(self):
        self.sqr_oval=self.pi *  (self.o**2)
        return self.sqr_oval

    def __str__(self)->str :
        return 'Sqr Oval ='+str(self.area())


o2 = ovals(3)
print(o2.area_o())


#%%
