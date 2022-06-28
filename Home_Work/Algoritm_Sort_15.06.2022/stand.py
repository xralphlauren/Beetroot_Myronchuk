import time
import sort1
import sort2
import random

raz = 100
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
    t1 = time.perf_counter()
    # начало алгоритма
    sort1.selection_sort(r)
    # конец алгоритма
    t2 = time.perf_counter()
    T1.append(t2 - t1)
    print(j, T1[-1])
    t1 = time.perf_counter()
    # начало алгоритма
    sort2.selection_sort(r)
    # конец алгоритма
    t2 = time.perf_counter()
    T2.append(t2 - t1)
    print(j, T2[-1])