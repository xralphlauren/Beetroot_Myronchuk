import time
import sort1
import sort2
import random


def stend(f, n, *args):
    count = 0

    for i in range(n):
        start = time.perf_counter()
        if f == 'sort':
            args[0].sort()
        else:
            f(*args)
        finish = time.perf_counter()
        count += finish - start

    return count/n

def cyc():
    n = 100
    f = open('../1.txt', 'a')
    for i in range(n):
        for j in range(n):
            f.write('1')
    f.close()


print(stend(cyc, 10))

raz = 1008
k = range(raz)
N = [10000, 20000, 30000]
T1 = []
T2 = []
test_file = 'max.csv'
# sort1.selection_sort(N)
# sort2.selection_sort(N)
for j in N:
    r = list(range(j))
    random.shuffle(r)
    print()


    print(f'sort1 для {j}, {stend(sort1.selection_sort, 2, r)}')
    print(f'sort2 для {j}, {stend(sort2.selection_sort, 2, r)}')
    print(f'sorted() для {j}, {stend(sorted, 2, r)}')
    print(f'sort() для {j}, {stend("sort", 2, r)}')