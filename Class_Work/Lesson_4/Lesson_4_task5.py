import math

a = int(input())

for i in range(a):
    for j in range(a):
        if math.gcd(i,j) == 1:
            print('*',end='')
        else:
            print(j,end='')
    print()



