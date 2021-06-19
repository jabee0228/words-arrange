

def returnlastchar(s):
    return s[10:]

z = 1
a = []
for i in range(150):
    z = input()
    if z == '0':
        break
    a.append(z)
a.sort()
decorated = [(returnlastchar(s), s) for s in a]
decorated.sort()
a = [x[1] for x in decorated]

for i in range(len(a)):
    print(a[i])