# public can be use,within the class, in derived class and outside the  class to

class Student:

    def __init__(self,name):
        self.name = name

    def display(self):
        print(f"Hi, I am {self.name} from student class")


s1 = Student("Rohit")
print(s1.name)
s1.display()
        
