class Person:
    count = 0
    staff = 0
    all_salary = 0
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title
        self.__class__.count += 1
        if self.status != 'Detailee':
            self.__class__.staff += 1
        self.__class__.all_salary += self.salary

    def __repr__(self):
        return self.name


class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)
        
    def get_sotr(self, name_file):
        f = open(name_file, 'r')
        t = f.readlines()
        f.close()
        for s in t[1:]:
            sp = s.strip().split(';')
            k = sp[2]
            salary = float(k.strip().replace('$','').replace(',',''))
            p = Person(sp[0], sp[1], salary, sp[3], sp[4])
            self.sotr.append(p)
    
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary
            
        return su/len(self.sotr)
        
    def top10(self):
        
        def sal(i):
            return i.salary
            
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse=True)
        
        return top2[:10]

    def detailees(self):        
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):        
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)

    def all_salary(self):
        Person.all_salary = sum([i.salary for i in self.sotr])
    
wh = WH('white_house_2017_salaries_com.csv')
#
print(wh.sotr[3], wh.sotr[3].salary, type(wh.sotr[3].salary))
print(wh.top10())
for i in wh.top10():
    print(i.name , i.salary)

print(wh.detailees())
print(wh.staff())

# task 1
print(Person.count)

# task 2
print(Person.staff)

# task 3
print(Person.all_salary)

# task 4
wh.sotr[5].salary = 50000000
wh.all_salary()
print(Person.all_salary)

