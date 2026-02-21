class Circle:

    # pi = 3.14 ya tho idar de sakta h 

    def __init__(self,radius,pi = 3.14):
        self.radius = radius
        self.pi = pi

    def get_circumference(self):
        return 2*self.pi*self.radius
    
    def get_area(self):
        return self.pi * self.radius**2
    


c1 = Circle(4)
print(c1.get_circumference())

c2= Circle(4)
print(c2.get_area())
        