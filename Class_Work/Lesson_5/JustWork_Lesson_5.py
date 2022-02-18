set = {3, 5.6, True, 'apple'}
print(set)
set.add('add_1')
set.add(7)

print(set)

set.update('update_1', 'update_2', 'update_3', [50, 51, 52]) #можемо додавати стрінги, тапли, лісти, але воно розбиває по елементах
print(set)

set.remove(True) #прибирає елемент за назвою (видає ерор, якщо немає такого елементу)
print(set)

set.discard(2) #прибирає елемент за назвою (не видає ерор, якщо немає такого елементу)
print(set)

x = set.pop() # видаляє 1 елемент і записує його в іншу змінну (невідомо, який елемент буде першим)
print('x ==>', x, '\n', set)

set_2 = {500, 700, 800, 'add_1', 3}
print(set.intersection(set_2))#показує елементи, які повторюються в обох сетах
print(set.difference(set_2))#прибирає елементи з першого сету, які повторюються в обох сетах
print(set.union(set_2))#об'єднання двох сетів

print(set&set_2) # intersection
print(set-set_2) # difference
print(set|set_2) # union

set_3 = set.copy()
print(set_3)

set_4 = {45, 6.7, 89, 7.4} #знаходимо найбільший і найменший елементи
print(max(set_4))
print(min(set_4))

for i in set_3:
    print(i, ',', end='')
print()

print(len(set_4))

set_4.clear()
print(set_4)

lst = list(set_3)

print(lst, type(lst))

print(set_3)
if 50 in set_3:
    print('Yes')