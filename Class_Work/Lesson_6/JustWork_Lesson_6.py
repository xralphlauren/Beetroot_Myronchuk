a = ['apple', 'lemon', 12345]
b = a.copy()
print(a)
print(b)
a.append('STR')
print(a)
print(b)


################

squares = list(map(lambda x: x**2, range(10)))
print(squares)

squares = [x**2 for x in range(10)]
print(squares)

###
squares = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(squares)

# тоже самое что и верхний скрипт, но длинее
res = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        res.append(x, y)
print(res)

###

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matrix_res = [[row[i] for row in matrix] for i in range(4)]
print(matrix_res)
# работает цикл так: [0][0], [1][0], [2][0]

###

a_dict = {
    'lst_1': [1, 2, 3, 4, 5]
}
print(a_dict.get('lst_1'))
a_dict.get('lst_1').append(51)
print(a_dict.get('lst_1'))

for i in a_dict.values():
    for y in i:
        print(y, type(y))


x = 10
for i in [1,2,3,4,5]:
    if i % 2 == 0:
        break
    x -= i
else:
    x = 10
print(x)