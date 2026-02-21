class Demo:

    def __init__(self,name,address):
        self.name = name
        self.adr = address

    def display(self,subject_name):   #Methods ,not function beacuse they are inside a class
        print(f"Hi, I am {self.name} and I am currently learing OOPS IN {subject_name}")


obj1 = Demo("Rohit","Silchar")
print(obj1.adr)

obj1.display("Python")
        