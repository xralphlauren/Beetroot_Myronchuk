def check(x):
    if type(x) == list:
        out_lst = list()
        for i in x:
            out_lst.append(i.__code__.co_nlocals)
        return out_lst
    else:
        return x.__code__.co_nlocals


def variant_1():
    a = [1, 2, 3]
    b = 'privet'
    d = {1: '1', 2: '2', 3: '3'}


def variant_2():
    a = ['a', 'b', 'c', 'd', 'e']
    b = 'privet1'
    c = 'privet2'
    d = 'privet3'
    e = 'privet4'
    f = 'privet5'


print(check(variant_1))
lst_variant = [variant_1, variant_2]
print(check(lst_variant))

