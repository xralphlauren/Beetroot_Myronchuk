class Dog:
    def __init__(self, inp_age_dog):
        self.age_dog = inp_age_dog

    def human_age(self):
        return int(self.age_dog) * 7


a = Dog(5)
print(a.human_age())
