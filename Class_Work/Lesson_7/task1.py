import random


def func_1(*args):
    count = 1
    max_count = 1
    pos_count = args[0][0]
    for i in range(len(args[0])-1):
        if args[0][i] == args[0][i+1]:
            count += 1
        if count > max_count:
            max_count = count
            pos_count = args[0][i]
        if args[0][i] != args[0][i+1]:
            count = 1
    return max_count, '>>>', pos_count


n = [random.randint(1, 10) for i in range(random.randint(1, 10))]


print(n)
print(func_1(n))
