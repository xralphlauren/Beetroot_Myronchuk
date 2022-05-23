import functools

def dec(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        return '<b>' + f + '</b>'

    return wrapper

@dec
def privet():
    return 'PREVED!'


print(privet())

for k in globals():
    print(k, globals()[k])