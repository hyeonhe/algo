s = int(input())

for i in range(1, 4294967295):
    num = (i * (1 + i) // 2)
    if num > s:
        print(i - 1)
        break