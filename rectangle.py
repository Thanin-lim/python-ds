from Shapes import Shape

class rectangle(Shape):

    def __init__(self,w,l):
        self.sqr_tangle=0.0
        self.w=w
        self.l=l
    def area(self):
        self.sqr_tangle=self.w*self.l
        return self.sqr_tangle
    def __str__(self)->str:
        return 'Square Area 4 rectangle  '+  str(self.area())



#%%
