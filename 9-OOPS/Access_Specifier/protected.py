# Protrctrd can be acces within the class and derived class only

class Student:

    def __init__(self,name,rollno):
        self.name = name #public 
        self._rollno = rollno #protected

    def show(self):
        print(f"Hi, I am {self.name} and my rollno is : {self._rollno} from student class")


class Branch(Student):

    pass

b1 = Branch("Rohit",85)
print(b1.name)
print(b1._rollno)
b1.show()


s1 = Student("Akash",78)
print(s1.name)
print(s1._rollno)
s1.show()