# Make a program that has some sentence (a string) on input and returns a dict containing all unique words
# as keys and the number of occurrences as values.


a = 'A good breakfast is a good day'.split()
my_dict = dict()
for i in a:
    if i not in my_dict:
        my_dict[i] = a.count(i)

print(my_dict)