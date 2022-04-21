# task 1
import pet
import random


x = 10  # количество шагов
n = 10  # количество повторений
for i in range(n):
    pet.vpered(x)
    pet.golos(x)


# task 2
import dicer


# def 3
for i in range(10):
    dicer.dice()

# def 4
for i in range(10):
    dicer.graph_dice()

# def 5
for i in range(1, 11):
    dicer.universal_dice(i)

dicer.universal_dice()

# def 6
for i in range(5):
    lst_vedro = dicer.vedro_kubov(n=random.randint(6, 10), k=random.randint(2, 15))
    print(lst_vedro)
