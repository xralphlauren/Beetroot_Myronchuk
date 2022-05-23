class Person:
    def __init__(self, name, fam, gender, age):
        self.name = name
        self.fam = fam
        self.gender = gender
        self.age = age

    def person_hi(self):
        print(f'Я из класса Person Меня зовут {self.name} {self.fam}, я {self.gender} пола, мне {self.age} лет')


class Student(Person):
    def __init__(self, name, fam, gender, age, course, grade):
        Person.__init__(self, name, fam, gender, age)
        self.course = course
        self.grade = grade

    def Student_hi(self):
        Person.person_hi(self)
        print(f'Я студент из {self.course} курса, с {self.grade} грейдом')


class Teacher(Person):
    def __init__(self, name, fam, gender, age, salary, experience):
        Person.__init__(self, name, fam, gender, age)
        self.salary = salary
        self.experience = experience

    def Teacher_hi(self):
        Person.person_hi(self)
        print(f'Я учитель, мой стаж {self.experience} лет, моя заробаная плата {self.salary}')


# Проверка

student1 = Student('Karter', 'Perez', 'male',20, 2, 'A')
student2 = Student('Ulyses', 'Green', 'male', 21, 3, 'A')
st_lst = [student1, student2]

teacher1 = Teacher('Ivan', 'Rivera', 'male', 51, '10000$', 25)
teacher2 = Teacher('Allen', 'Cook', 'male', 35, '7000$', 12)
tc_lst = [teacher1,teacher2]

person1 = Person('Orson', 'Anderson', 'male', 27)

for i in st_lst:
    i.Student_hi()
for i in tc_lst:
    i.Teacher_hi()
person1.person_hi()
teacher1.person_hi()