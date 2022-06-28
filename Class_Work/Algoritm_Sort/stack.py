stack = []
stack.append(8)
stack.append(15)
stack.pop()


def factorial(n):
    stack = []
    f = 1

    while n > 0:
        stack.append(n)
        n = n - 1

    while len(stack) > 0:
        f = f * stack.pop()
    print(stack)

    return f

print(factorial(4))