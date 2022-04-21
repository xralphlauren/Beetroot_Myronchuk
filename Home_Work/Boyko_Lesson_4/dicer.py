import random


# task 3
def dice():
    return print(f'Кубик показал число: {random.randint(1,6)}')


# task 4
def graph_dice():
    x = random.randint(1, 6)
    dict = {
        1: '\u2680',
        2: '\u2681',
        3: '\u2682',
        4: '\u2683',
        5: '\u2684',
        6: '\u2685'
    }
    return print(dict[x])


# task 5
def universal_dice(x=6):
    w = random.randint(1, x)
    return print(f'Фигура с количеством граней: {x}, показала случайное число : {w}')



# task 6
def vedro_kubov(n=6, k=1):
    lst = []
    for i in range(k):
        w = random.randint(1, n)
        lst.append(w)
    return lst
