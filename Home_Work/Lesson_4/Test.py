

import random

a = input("Please enter random word: ")
finish_word = ''
check_index = ''
while len(a) != len(finish_word):
    b = random.randint(0, len(a)-1)
    if str(b) not in check_index:
        finish_word += a[b]
        check_index += str(b)
print(finish_word)

##########
#import random
#
#a = input("Please enter random word: ")
#c = ''
#while len(a) != len(c):
#    c += random.choice(a)
#
#print(c)
#

