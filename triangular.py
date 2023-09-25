from Shapes import Shape
class triangular(Shape):

    def __init__(self,w,h)->None:
        self.sqr_tr=0.0
        self.w=w
        self.h=h
        self.t=2
    def area(self):
        self.sqr_tr=(self.w*self.h)/self.t
        return self.sqr_tr
    def __str__(self)->str:
        return 'Square Triangular :'+str(self.area())
t1=triangular(20,30)
print(t1)
#%%
