todo = ['покодить в python', 'обновить таблицу sql', 'позаниматься спортом', 'поработать',
        'съездить за продуктами', 'приготовить ужин', 'почистить зубы']

print(todo[0], todo[2], todo[3], todo[-1], sep='\n')
print(todo[:3], todo[3:], sep='\n')

todo.append('какое-то дело')
todo.append('ещё какое-то дело')

todo[0], todo[-1] = todo[-1], todo[0]

todo.append(input('Введите ещё одно дело в список: '))

todo2 = todo
todo3 = todo[:]
todo4 = list(todo)
todo5 = todo.copy

