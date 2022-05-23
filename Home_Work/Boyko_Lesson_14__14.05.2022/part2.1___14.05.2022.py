# task 2.1
class GreatNumerator:
    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return gen_iterator(self.lst)


class gen_iterator:
    def __init__(self, lst):
        self.lst = lst
        self.c = -1

    def __next__(self):
        if self.c < len(self.lst)-1:
            self.c += 1
            return str(self.c) + ' ' + self.lst[self.c]
        else:
            raise StopIteration


lists = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(lists)
for i in t:
    print(i)


