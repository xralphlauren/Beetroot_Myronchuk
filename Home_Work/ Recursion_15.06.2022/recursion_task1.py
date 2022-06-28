def rev(st):
    if len(st) == 1:
        return st
    return st[-1] + rev(st[:-1])


assert rev('Бла-бла-бла') == 'алб-алб-алБ'

