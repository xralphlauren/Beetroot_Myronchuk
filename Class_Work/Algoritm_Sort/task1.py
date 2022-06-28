# n! = 1 * 2 * ... * n - 1 * n
# n! = 1

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# factorial(4)
# 4 * factorial(3)
# 4 * ( 3 * factorial(2)))
# 4 * ( 3 * ( 2 * factorial(1)))
# 4 * ( 3 * ( 2 * ( 1 * factorial(0)))
# 4 * ( 3 * ( 2 * ( 1 * 1 )))
# 4 * ( 3 * ( 2 * 1 ))
# 4 * ( 3 * 2 )
# 4 * 6
# 24


# 1 * 2 * 3 * 4 = 24
print(factorial(997))