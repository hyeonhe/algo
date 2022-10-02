x = []
y = []

for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

if x.count(x[0]) == 1:
    print(x[0], end=' ')
else:
    print(x[-1], end=' ')

if y.count(y[0]) == 1:
    print(y[0])
else:
    print(y[-1])