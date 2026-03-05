from collections import deque

d = deque()

d.append(1)
d.append(2)

print(d)

d.appendleft(3)
print(d)

# d.pop()
# print(d)

# d.popleft()
# print(d)


d.extend([4,5,6])
print(d)

d.extendleft([7.8,9])
print(d)

d.rotate(2)
print(d)

d.clear()
print(d)

