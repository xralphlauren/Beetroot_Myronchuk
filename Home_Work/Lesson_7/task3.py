def make_operation(operator, *args):
    count = args[0]
    for i in args[1:]:
        if operator == '-':
            count -= i
        elif operator == '+':
            count += i
        elif operator == '*':
            count *= i
    return count


print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))
