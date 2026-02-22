class Human:

    def __init__(self,heart):
        self.num_eyes = 2
        self.heart = heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I acn work")

class Male(Human):

    def __init__(self,name,heart):
        Human.__init__(self,heart)
        self.name =name
        

    def flirt(self):
        print("I can flirt")

class Boy(Male):

    def __init__(self, name, heart,dance):
        super().__init__(name,heart)  #other way 
        # Human.__init__(self, heart)
        # Male.__init__(self,name)
        self.dance = dance


    def sleep(self):
        print("I can sleep")

    def work(self):
        super().work()
        print("I can code")

class Programmer(Boy):

    def work(self):
        super().work()
        print("I can write program")

b1 = Boy("Rohit",1,"No")
print(b1.name, b1.heart, b1.dance)

b1.work()


# p1 = Programmer()

# p1.work()