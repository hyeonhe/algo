import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

nn = []
mm = []

for i in range(n):
    nn.append(list(map(int, input().split())))

    
for i in range(n):
    mm.append(list(map(int, input().split())))

    
for i in range(n):
    for j in range(m):
        print(nn[i][j] + mm[i][j], end=' ')
    print()