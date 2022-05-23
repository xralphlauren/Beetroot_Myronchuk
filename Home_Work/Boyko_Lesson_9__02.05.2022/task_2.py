def my_len(x):
    count = 0
    for i in x:
        count += 1
    return count


def check_len(x):
    if my_len(x) > 10:
        return f'В переменной больше 10 символов'
    else:
        return f'В переменной меньше 10 символов'


print(check_len('АбраКадабра'))
print(check_len('Енот'))


