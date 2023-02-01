n = int(input())
c = [0, 1, 0, 0]

for _ in range(n):
    a, b = map(int, input().split())
    c[a], c[b] = c[b], c[a]

for i in range(1, 4):
    if c[i] == 1:
        print(i)