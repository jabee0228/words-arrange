z = 1
a = []
for i in range(150):
    z = input()
    if z == '0':
        break
    a.append(z)
a.sort()
for i in range(len(a)):
    print(a[i])