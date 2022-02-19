#a = [
#    (1, 2, 7),
#    ('apple', 'orange'),
#    ('501', '502', '503'),
#    (723, 'mouse', True),
#    (501, 502, 503),
#    (1, 2, 7)
#]
#
#b = []
#for i in range(len(a)):
#    for y in range(len(a)):
#        if a[i] == a[y] and i != y and a[i] not in b:
#            b.append(a[i])
#
#print(b)


a = [
    (1, 2, 7),
    ('apple', 'orange'),
    ('501', '502', '503'),
    (723, 'mouse', True),
    (501, 502, 503),
    (1, 2, 7)
]

if a.count(a[0]) == len(a):
    print(a)