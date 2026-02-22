class Human:
    def __init__(self,num_heart):
        print("calling init from human")
        self.num_eyes = 2
        self.num_nose = 1
        self.heart = num_heart

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")

class Male:
    def __init__(self,name):
        print("calling init from male")
        self.name = name

    def flirt(self):
        print("I can flirt")

    def work(self):
        print("I can code")

class Boy(Human,Male):
    def __init__(self,name,heart,language):
        Male.__init__(self,name)
        Human.__init__(self,heart)
        self.language = language

    def sleep(self):
        print("I can sleep")

    def work(self):
        print("I can test")

    def display(self):
        print(f"Hi, I am {self.name} and I have only {self.heart} HEART, thats belong to {self.language}")


B1 = Boy("Rohit",1,"Python")
# print(B1.num_eyes)
# print(B1.name)
# print(f"i have only {B1.heart} heart")
# print(B1.language)

# B1.display()
# B1.eat()
# B1.work()
# Male.work(B1)
# Human.work(B1)

Male.work(B1)
Human.work(B1)