from itertools import product

a = [2,3]
b = [1,4]

prod = product(a,b)
print(list(prod))

print(" ")

prod = product(a,b,repeat=2)
print(list(prod))