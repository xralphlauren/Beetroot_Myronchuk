import random

a = random.randint(1, 100)
b = random.randint(1, 100)
c = a + b


answer = int(input(f'Please enter your answer {a} + {b} = '))
if c == answer:
    print('Congratulations ! Your answer is correct')
else:
    print('Answer is not correct')






