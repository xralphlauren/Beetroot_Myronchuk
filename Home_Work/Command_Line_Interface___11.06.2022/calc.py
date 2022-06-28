import sys


args = sys.argv
args[1], args[2] = int(args[1]), int(args[2])
write_file = ''

if '-h' in args:
    if args[3] == '-':
        print(f'{args[1]} - {args[2]} = {args[1] - args[2]}')
        write_file = f'{args[1]} - {args[2]} = {args[1] - args[2]}'

    if args[3] == '+':
        print(f'{args[1]} + {args[2]} = {args[1] + args[2]}')
        write_file = f'{args[1]} + {args[2]} = {args[1] + args[2]}'

    if args[3] == '/':
        print(f'{args[1]} / {args[2]} = {args[1] / args[2]}')
        write_file = f'{args[1]} / {args[2]} = {args[1] / args[2]}'

    if args[3] == '*':
        print(f'{args[1]} * {args[2]} = {args[1] * args[2]}')
        write_file = f'{args[1]} * {args[2]} = {args[1] * args[2]}'

    if args[3] == '**':
        print(f'{args[1]} ** {args[2]} = {args[1] ** args[2]}')
        write_file = f'{args[1]} ** {args[2]} = {args[1] ** args[2]}'

else:
    if args[3] == '-':
        print(args[1] - args[2])
        write_file = args[1] - args[2]

    elif args[3] == '+':
        print(args[1] + args[2])
        write_file = args[1] + args[2]

    elif args[3] == '/':
        print(args[1] / args[2])
        write_file = args[1] / args[2]

    elif args[3] == '*':
        print(args[1] * args[2])
        write_file = args[1] * args[2]

    elif args[3] == '**':
        print(args[1] ** args[2])
        write_file = args[1] ** args[2]

if '-f' in args:
    name_file = args[args.index('-f') + 1]
    f = open(name_file, 'w')
    f.write(str(write_file))
    f.close()