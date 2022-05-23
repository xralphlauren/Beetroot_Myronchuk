class Person:
    def __init__(self, inp_name, inp_fam, inp_age):
        self.name = inp_name
        self.fam = inp_fam
        self.age = inp_age

    def talk(self):
        print(f'Привет, меня зовут {self.name} {self.fam}, и мне {self.age} лет')


a = Person('Dima', 'Myronchuk', 25)
a.talk()
