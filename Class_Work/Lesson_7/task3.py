import random


def func(*args):
    a = []
    for i in args:
        if args.count(i) > 1 and i not in a:
            a.append(i)
    return a


n = [random.randint(1, 10) for i in range(random.randint(1, 10))]
print(n)
print(func(*n))


