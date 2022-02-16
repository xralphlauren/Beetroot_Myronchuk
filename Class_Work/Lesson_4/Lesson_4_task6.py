a = input('Enter temperature in format f** or c**: ')
b = ''
answer = ''
if a[0] == 'c':
    for i in range(1,len(a)):
        b += a[i]
    b = float(b)
    answer = b * 1.8 + 32
    print(answer)
if a[0] == 'f':
    for i in range(1,len(a)):
        b += a[i]
    b = float(b)
    answer = (b - 32) / 1.8
    print(answer)
