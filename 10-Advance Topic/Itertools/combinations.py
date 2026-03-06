from itertools import combinations,combinations_with_replacement

a = [1,2,3,4]
comb = combinations(a,3)

print(list(comb))

comb_wr = combinations_with_replacement(a,3)
print(list(comb_wr))