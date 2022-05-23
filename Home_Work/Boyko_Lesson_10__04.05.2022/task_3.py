def arg_rules(type_: type, max_length: int, contains: list):
    def mydec(func):
        def wrapper(*args, **kwargs):
            switch = True
            f = func(*args, ** kwargs)
            if len(args[0]) > max_length:
                switch = False
            if type(args[0]) != type_:
                switch = False
            for i in contains:
                if i not in args[0]:
                    switch = False
            if switch == True:
                return f
            if switch == False:
                return False
        return wrapper
    return mydec


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

