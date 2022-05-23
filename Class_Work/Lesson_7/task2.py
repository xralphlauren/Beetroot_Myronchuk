import random

# Variant 1 with set
def func_1(*args):
    a = []
    for i in args:
        a.append(i)
    a = list(set(a))
    return a



# Variant 2 without set

def func_2(*args):
    a = []
    for i in args:
        if i not in a:
            a.append(i)
    return a


n = [random.randint(1, 10) for i in range(random.randint(1, 10))]

print(n)
print(func_1(*n))
print(func_2(*n))
