file = open('access-log', 'r')
read = file.readlines()
file.close()

sm = 0
for i in read:
    if i.split()[-1].isdigit():
        sm += int(i.split()[-1])

print(sm)

