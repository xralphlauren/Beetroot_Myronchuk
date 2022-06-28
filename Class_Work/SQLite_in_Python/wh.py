import sqlite3


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
        self.__class__.all_salary += self.salary
        if self.status != "Detailee":
            self.__class__.staff += 1
    
    def __del__(self):
        self.__class__.count -= 1
        self.__class__.all_salary -= self.salary
        if self.status != "Detailee":
            self.__class__.staff -= 1   
            
    def __repr__(self):
        return self.name
    
    def return_list_fields(self):
        return ["name", "status", "salary", "pay_basis", "position_title"]

    def secret_agent(cls, name):
        return cls(name, 'secret agent', 0, 'classified', 'classified')

    def superman(cls, name):
        return cls(name, 'super staff', 100000, 'monthly', 'super hero')
        
    def people(cls):
        print(f'''Всего {cls.count} сотрудников, 
из них {cls.staff} на постоянной основе
общий заработок {cls.all_salary}''')

    #def hi():
    #    print('Привет, я статический метод')
        
class NewPerson(Person):
    def __init__(self, name, location):
        Person.__init__(self, name,  'super staff', 100000, 'monthly', 'super hero')
        self.location = location

n = NewPerson('James Bond', 'London')


class WH:
    def __init__(self, name_file):
        self.sotr = []
        self.get_sotr(name_file)

    def save_to_sql(self, name_sql):
        con = sqlite3.connect(name_sql)
        cur = con.cursor()
        cur.execute('''CREATE TABLE sotr
                    (name text,
                     status text,
                     salary real,
                     pay_basis test,
                     position_title text)''')
        for s in self.sotr:
            query = f'''INSERT INTO sotr 
                        VALUES("{s.name}",
                               "{s.status}",
                               {s.salary},
                               "{s.pay_basis}",
                               "{s.position_title}")'''
            print(query)
            cur.execute(query)
        con.commit()
        con.close()


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
    
    def recount(self):
        su = 0
        for s in self.sotr:
            su += s.salary
        Person.all_salary = su
        
    
    def summa(self):
        su = 0
        for s in self.sotr:
            su += s.salary
            
        return su/len(self.sotr)
        
    def top10(self):
        
        def sal(i):
            return i.salary
            
        top = self.sotr.copy()
        top2 = sorted(top, key=sal, reverse = True)
        
        return top2[:10]

    def detailees(self):        
        return [i for i in self.sotr if i.status == 'Detailee' ]
        
    def staff(self):        
        return len([i for i in self.sotr if i.position_title == 'STAFF ASSISTANT' ])
        
    def rep(self):
        for i in self.sotr:
            print(i)
            
    def count_sotr(self):
        print(f'''Всего {Person.count} сотрудников, 
из них {Person.staff} на постоянной основе
общий заработок {Person.all_salary}''')
