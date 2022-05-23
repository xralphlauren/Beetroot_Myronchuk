def logger(func):
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        print(f'called {func.__name__} and the function has arguments {args} and {kwargs}')
        return f
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(5, 7)
square_all(5, 16, 1234, 213)