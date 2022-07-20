import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
red = []
green = []
blue = []

for i in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b)

r = [0] * n
g = [0] * n
b = [0] * n
r[0] = red[0]
g[0] = green[0]
b[0] = blue[0]
result = 0

for i in range(1, n):
    r[i] = min(g[i-1] + red[i], b[i-1] + red[i])
    g[i] = min(r[i-1] + green[i], b[i-1] + green[i])
    b[i] = min(r[i-1] + blue[i], g[i-1] + blue[i])

print(min(r[-1], g[-1], b[-1]))