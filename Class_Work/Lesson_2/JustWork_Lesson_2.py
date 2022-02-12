x = 30
y = '50'
print(x + int(y))

str = 'Dima is great DEVELOPER!'
print(str.find('great'))
print(str.index('great'))

super_power = '111'
enemy = '222'
name = '333'
print('Superhero name is {1}, his super power - {0}, his enemy - {2}'.format(super_power, enemy, name))


message = 'Hello beautiful world!'
final_message = message[0:5] + ' ' + message[-6:] + ' Today is a ' + message[6:15] + ' day.'
print(final_message)