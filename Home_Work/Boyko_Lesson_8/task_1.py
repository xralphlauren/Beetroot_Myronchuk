class Animal:
    def talk(self):
        print(f'Hi I\'m an animal')

class Dog(Animal):
    def talk(self):
        print(f'woof woof')


class Cat(Animal):
    def talk(self):
        print(f'meow meow')


a = Animal()
d = Dog()
c = Cat()
e = Dog()
f = Cat()
lst = [a, d, c, e, f]

for i in lst:
    i.talk()
