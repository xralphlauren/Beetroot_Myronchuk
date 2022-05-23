'''class GreatNumerator:
    def __init__(self,lst):
        self.lst = lst

    def task(self):
        for i in self.lst:
            yield f'{self.lst.index(i)} {i}'


strings = ['111', 'cat', 'got', 'ddd', '222']
t = GreatNumerator(strings).task()
for i in t:
    print(i)
'''


def Phonefil(lst):
    for i in lst:
        yield f'{lst.index(i)} {i}'


strings = ['111', 'cat', 'got', 'ddd', '222']

for i in Phonefil(strings):
    print(i)