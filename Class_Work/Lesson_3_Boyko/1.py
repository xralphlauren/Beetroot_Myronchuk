import urllib.request

f = urllib.request.urlopen('http://example.com/')
t = f.readlines()
f.close()

print(t)

j = open('')