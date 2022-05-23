def funn(s):
    for i in range(len(s)):
        if s[i].isdigit():
            pass
        else:
            yield s[i]



k = funn('3к2о1т')
print(k)

for i in k:
    print(i)


k = funn('к5и111231т')
print(k)

print([i for i in k])