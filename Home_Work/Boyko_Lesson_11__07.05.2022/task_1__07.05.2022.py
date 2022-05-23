import copy


class Employee:
    def __init__(self, name, status, salary, pay_basis, position_title):
        self.name = name
        self.status = status
        self.salary = salary
        self.pay_basis = pay_basis
        self.position_title = position_title

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class WH:
    def __init__(self, file_path):
        self.list_sotr = []

        file = open(file_path, 'r')
        read = file.readlines()

        for i in read[1:]:
            ispl = i.split(';')
            self.list_sotr.append(Employee(ispl[0], ispl[1], ispl[2].replace(',', '').replace('$', ''), ispl[3], ispl[4]))

    def mid_salary(self):
        ms = [float(i.salary) for i in self.list_sotr]
        return f'Средняя заработная плата в белом доме составляет: ${sum(ms)/len(ms)}'

    def change_position(self):
        lst = [i for i in self.list_sotr if i.status == 'Detailee']
        return f'Количество людей назначеных на временную должность составляет: {len(lst)}'

    def count_staff(self):
        lst = [i for i in self.list_sotr if 'STAFF ASSISTANT' in i.position_title]
        return f'Количество людей на должности STAFF ASSISTANT составляет: {len(lst)}'

    def mid_salary_staff(self):
        lst = []
        [lst.append(float(i.salary)) for i in self.list_sotr if 'STAFF ASSISTANT' in i.position_title]
        return f'Средняя заработная плата людей на должности STAFF ASSISTANT составляет: ${sum(lst)/len(lst)}'

    def count_position(self):
        lst = []
        # i.position_title[:-2] - убираю символ \n
        [lst.append(i.position_title[:-2]) for i in self.list_sotr if i.position_title[:-2] not in lst]
        return f'Всего в белом доме: {len(lst)} дожностей и вот и перечень: {lst}'

    def ppl_in_position(self):
        dct = dict()
        for i in self.list_sotr:
            if i.position_title not in dct:
                dct[i.position_title] = 1
            else:
                dct[i.position_title] += 1
        return f'Список людей на каждой должности: {dct}'

    def top_10_salary(self):
        top_lst = []
        lst_copy = copy.deepcopy(self.list_sotr)                        # Создаю копию списка,чтобы не испортить ориг.

        for i in range(10):
            top_salary = max([float(i.salary) for i in lst_copy])       # получаю сумму топ зп в каждом цикле

            for j in lst_copy:
                if float(j.salary) == top_salary:                       # Когда нахожу одного из людей с максимальной зп
                    a = lst_copy.pop(lst_copy.index(j))                 # в этом цикле, убираю его из списка и добавляю
                    top_lst.append(a)                                   # в другой список
                    break

        return f'Список людей с заработной платой TOP 10: {top_lst}'


w = WH('white_house_2017_salaries_com.csv')


print(w.mid_salary())
print(w.change_position())
print(w.count_staff())
print(w.mid_salary_staff())
print(w.count_position())
print(w.ppl_in_position())
print(w.top_10_salary())
