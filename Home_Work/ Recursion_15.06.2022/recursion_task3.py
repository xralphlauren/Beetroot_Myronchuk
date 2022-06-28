def str_sum(chislo):
    if chislo.isdigit():
        if len(chislo) == 1:
            return chislo
        return int(chislo[-1]) + int(str_sum(chislo[:-1]))
    else:
        raise ValueError("Sorry, function only accepts digits")


a = '12345'
assert str_sum(a) == 15

