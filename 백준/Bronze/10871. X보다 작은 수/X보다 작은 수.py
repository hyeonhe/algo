n, x = input().split()
n = int(n)
x = int(x)
listA = []

listA = list(map(int, input().split()))

for i in range(n):
    if listA[i] < x:
        print(listA[i], end=' ')
