def smallest(m):
    min_m = m[0]    # стартовый елемент
    min_n = 0       # индекс стартового елемента
    for n, i in enumerate(m):
        if i > min_m:
            min_m = i
            min_n = n
    return min_n






def sort_by_choice(m):
    sorted_m = []
    m1 = m.copy()
    while len(m1) > 0:
        n = smallest(m1)


k = [1,3,9,2,4]
print(sort_by_choice(k))