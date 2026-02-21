class Demo:

    def __init__(self,name,address):

        self.name = name
        self.adr = address

        print("Creating a new object")


obj1 = Demo("Rohit","Silchar")
print(obj1.name)

obj2 = Demo("Akash","Bhopal")
print(obj2.name)
print(obj2.adr)