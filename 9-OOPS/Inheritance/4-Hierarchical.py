class Human:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def ShowDetails(self):
        print(f"name: {self.name}, age: {self.age}")

    def eat(self):
        print("I can eat")

class Male(Human):

    def sleep(self):
        print("I can sleep")

class Female(Human):

    def work(self):
        print("I can work")

f1 = Female("Shayani",20)
# f1.work()
f1.ShowDetails()

# m1 = Male()
# m1.eat()