list = []
while True:
    a, b = map(int, input().split())
    if a == 0 or b == 0:
        break
    list.append(a+b)

for i in range(len(list)):
    print(list[i])
