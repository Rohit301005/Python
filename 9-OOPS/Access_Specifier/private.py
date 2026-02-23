# can be access only inside the class

class Student:

    def __init__(self,name,rollno,age):
        self.name = name #public 
        self._rollno = rollno #protected
        self.__age = age #private

    def __show(self):
        print(f"Hi, I am {self.name} and my rollno is : {self._rollno} & my age is : {self.__age} from student class")

    def display(self):
        self.__show()

s1 = Student("Rohit",85,20)
s1.display()  # one way to calling a private variable


print(" ")

# other way to calling
print(s1._Student__age)
s1._Student__show()