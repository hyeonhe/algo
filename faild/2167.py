n, m = map(int, input().split())
array = [[] for i in range(n)]

for i in range(n):
    for j in range(m):
        array[i].append(int(input()))

k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())
    ans = 0
    