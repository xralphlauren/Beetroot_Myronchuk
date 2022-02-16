import random

count = 0
while count != 5:
    a = random.randint(10, 1000)
    if a % 7 == 0:
        print(a)
        count += 1