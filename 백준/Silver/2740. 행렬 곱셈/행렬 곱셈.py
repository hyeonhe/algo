n, m = map(int, input().split())
a = []
b = []

for i in range(n):
    a.append(list(map(int, input().split())))

m, k = map(int, input().split())

for i in range(m):
    b.append(list(map(int, input().split())))

c = [[0 for _ in range(k)] for i in range(n)]

for i in range(n):
    for j in range(k):
        for h in range(m):
            c[i][j] += a[i][h] * b[h][j]

for i in c:
    for j in i:
        print(j, end = ' ')
    print()