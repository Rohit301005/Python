class Student:

    def __init__(self,name,rollno,age):
        self.name = name
        self._rollno = rollno
        self.__age = age

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age


s1 = Student("Rohit",85,20)

print(s1.get_age())

s1.set_age(21)

print(s1.get_age())