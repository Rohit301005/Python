from itertools import permutations

a = [1,2,3]

perm = permutations(a)
print(list(perm))

print(" ")

perm = permutations(a,2)
print(list(perm))