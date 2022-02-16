# Create a program that reads an input string and then creates and prints 5 random strings
# from characters of the input string.

# For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters
# ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …

#Tips: Use random module to get random char from string)

import random

a = input("Please enter random word: ")
for i in range(5):
    finish_word = ''
    while len(a) != len(finish_word):
        b = random.choice(a)
        if a.count(b) > finish_word.count(b):
            finish_word += b
    print(finish_word)
