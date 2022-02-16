# Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.


import random
a = 0
b = 1
while a != b:
    a = random.randint(1, 10)
    b = int(input("Введите число от 1 до 10: "))
    if b == a:
        print('Random selected number', str(a) + '.', 'Congratulations! You guessed a random number')
        break
    else:
        print('Random selected number', str(a) + '.', 'Try again')
