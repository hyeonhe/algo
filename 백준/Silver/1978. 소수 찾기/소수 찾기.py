n = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(len(a)):
    divcount = 0
    for j in range(1, a[i] + 1):
        if a[i] % j == 0:
            divcount += 1
    if divcount == 2:
        count += 1

print(count)