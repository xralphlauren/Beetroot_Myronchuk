Address_Book = {
    'Natalia': ['Vinnitsa, st. Shevchenko 17', 53],
    'Aleksey': ['Kyiv, st. Bessarabskaya 5',47],
    'Dima': ['Kyiv, st. Chernobulska 21', 51]
}

def func():
    close = input('Do you want to continue working with the address book\n'
                  'if yes - please press - yes\n'
                  'if no - please press - no\n'
                  'yes/no: '
                  )
    if close.upper() == 'YES':
        return 'continue'
    if close.upper() == 'NO':
        return 'break'



while True:
    print('Hello. Its a Address Book')
    print('You can use following function:\n'
          '1 - See the address of the person you need\n'
          '2 - Add new contact to address book\n'
          '3 - Calculate average of all contacts friends\n'
          '4 - Delete contact in address book\n'
          )
    a = input('Enter the number of the action you want: ')
    if a == '1':
        name = input('Enter name: ')
        name_print = Address_Book.get(name, 'This name is not in our address book.')
        print(name_print)
        #close = input('Do you want to continue working with the address book\n'
        #              'if yes - please press - yes\n'
        #              'if no - please press - no\n'
        #              'yes/no: '
        #              )
        #if close.upper() == 'YES':
        #    continue
        #if close.upper() == 'NO':
        #    break
        if func() == 'continue':
            continue
        if func() == 'break':
            break
    elif a == '2':
        name = input('Enter name: ')
        address = input('Enter address: ')
        count_friends = int(input('Enter number of friends: '))
        Address_Book[name] = [address, count_friends]
        close = input('Do you want to continue working with the address book\n'
                      'if yes - please press - yes\n'
                      'if no - please press - no\n'
                      'yes/no: '
                      )
        if close.upper() == 'YES':
            continue
        if close.upper() == 'NO':
            break
    elif a =='3':
        count = 0
        for key,value in Address_Book.items():
            count += value[1]
        print(count/len(Address_Book))
        close = input('Do you want to continue working with the address book\n'
                      'if yes - please press - yes\n'
                      'if no - please press - no\n'
                      'yes/no: '
                      )
        if close.upper() == 'YES':
            continue
        if close.upper() == 'NO':
            break
    elif a == '4':
        name = input('Enter the name of the contact you want to delete: ')
        Address_Book.pop(name)
        close = input('Do you want to continue working with the address book\n'
                      'if yes - please press - yes\n'
                      'if no - please press - no\n'
                      'yes/no: '
                      )
        if close.upper() == 'YES':
            continue
        if close.upper() == 'NO':
            break



