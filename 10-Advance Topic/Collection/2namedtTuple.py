from collections import namedtuple

Preson = namedtuple("Preson","name,age,city")
p = Preson("Rohit",20,"Silchar")

print(p)

print(p.name)
print(p.age)
print(p.city)