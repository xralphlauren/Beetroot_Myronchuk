a = input()
digital = 0
Word = 0
for i in a:
    if i.isdigit():
        digital += 1
    elif i.isalpha():
        Word += 1
print(digital, Word)