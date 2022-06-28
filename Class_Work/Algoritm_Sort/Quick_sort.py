def sorting(a):
    if len(a) <= 1:
        return a
    else:
        # выбираем опорный елемент
        op = a.pop()  # a[-1]
        lesser = []
        bigger = []

        for i in a:
            if i < op:
                lesser.append(i)
            else:
                bigger.append(i)

        les = sorting(lesser)
        big = sorting(bigger)

        return les + [op] + big

print(sorting([51, 72, 5, 21312, 1, 4 , 15, 123, 23, 5]))