class N:

    counter = 0

    def __init__(self):
        self.i = 1
        self.__class__.counter +=1

    def hi(self):
        print('Привет')

    def rep(self):
        print(f'Всего {self.__class__.counter} обьектов')


n = N()
n1 = N()
s = []
for i in range(100):
    s.append(N())

n.rep()
