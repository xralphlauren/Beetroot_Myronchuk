import sys
version = '0.0.1'
args = sys.argv


print(args)

if '-h' in args:
    print('Помогите ! ! !')
    
if '-v' or '--version' in args:
    print(f'Демонстратор v{version}')