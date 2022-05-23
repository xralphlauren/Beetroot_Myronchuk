from functools import wraps

def red(func):
    def wrapper(*args, **kwargs):
        f = '<font color="red">' + func(*args, **kwargs) + '</font>'
        return f
    return wrapper


def green(func):

    def wrapper(*args, **kwargs):
        f = '<font color="green">' + func(*args, **kwargs) + '</font>'
        return f

    return wrapper


def bold(func):
    @wraps(func) # для сейва имени
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        return f'<b>{f}</b>'
    return wrapper


#@green
#@red
@bold
def hi(name):
    return f'Привет {name}'






def color(cvet):
    def red(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            f = f'<font color="{cvet}">' + func(*args, **kwargs) + '</font>'
            return f
        return wrapper
    return red


@color('black')
def print_account():
    # много много вычислений
    return 'Я отчет за год'


#hi = green(hi)
#hi = red(hi)
print(hi('Дмитрий'))

print_account = green(print_account)
print(print_account())
