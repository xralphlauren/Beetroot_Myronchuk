import random


# task 1
def square(x):
    perimeter = x * 4
    square = x ** 2
    diagonal = x * (2 ** 0.5)
    return perimeter, square, diagonal


for i in range(5, 8):
    print(square(i))

# task 2
def season(x):
    if x.isdigit() and 0 < int(x) <= 12:
        x = int(x)
        if x <= 2 or x == 12:
            return print('Зима')
        if 3 <= x <= 5:
            return print('Весна')
        if 6 <= x <= 8:
            return print('Лето')
        if 9 <= x <= 11:
            return print('Осень')
    else:
        return print('Вы ввели не корректное значение')


for i in range(1,13):
    print(i, end=' ')
    season(str(i))


# task 3
def dice():
    return print(f'Кубик показал число: {random.randint(1,6)}')


for i in range(10):
    dice()


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


for i in range(10):
    graph_dice()


# task 5
def universal_dice(x=6):
    w = random.randint(1, x)
    return print(f'Фигура с количеством граней: {x}, показала случайное число : {w}')


for i in range(1, 11):
    universal_dice(i)

universal_dice()


# task 6
def vedro_kubov(n=6, k=1):
    lst = []
    for i in range(k):
        w = random.randint(1, n)
        lst.append(w)
    return lst


for i in range(5):
    lst_vedro = vedro_kubov(n=random.randint(6, 10), k=random.randint(2, 15))
    print(lst_vedro)