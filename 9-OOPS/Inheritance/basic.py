class Human:

    def __init__(self,num_heart):
        self.num_eye = 2
        self.num_nose = 1
        self.num_heart = num_heart

    def eat(self):
        print("I can eat")

    def  work(self):
        print("I acn work")


class Male(Human):
    
    def  __init__(self,name,heart):  #method overriding
        super().__init__(heart)    #using supper keyword we can access method from base class if it already override
        self.name = name

    def work(self):  #method overriding
        super().work()
        print("I can code")

    def flirt(self):
        print("I can flirt")

    def display(self):
        print(f"Hi, I am {self.name},and i have only {self.num_heart} heart")
     

m1 = Male("Rohit",1)
m1.work()
print(m1.num_eye)
print(m1.name)
m1.flirt()

h1 = Human(1)
h1.eat()

m1.display()