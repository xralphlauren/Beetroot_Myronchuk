# infiniti loop
# категории возрастов

while True:
    print('To start the loop, write "Yes"')
    go = input('Lets go?: ')
    if go == 'Yes' or go == 'yes':
        Age = int(input('How old are you: '))
        if Age <= 5:
            print('Hello baby')
        if 5 < Age <= 15:
            print('did you do homework?')
        if 15 < Age <= 25:
            print('bro you need more learning')
        if 25 < Age <= 40:
            print('go to hard Work ! ! !')
        if 40 < Age:
            print('Just chill')
    else:
        print('Good luck a day ! ! !')
        break





