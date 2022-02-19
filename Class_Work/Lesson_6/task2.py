a = [
    (1, 2, 7),
    ('apple', 'orange'),
    (),
    (723, 'mouse', True),
    ()
]

for i in a:
    if len(i) == 0:
        a.remove(i)
print(a)
