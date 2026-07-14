def greater_first(func):
    def wrap(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return wrap

@greater_first
def sub(a,b):
    return a-b

@greater_first
def divide(a,b):
    return a/b

print(sub(2,4))
print(divide(2,4))