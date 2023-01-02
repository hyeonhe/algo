import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
cnt = []

for a in range(n - 7):
    for b in range(m - 7):
        idx = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if array[i][j] == 'W':
                        idx += 1
                else:
                    if array[i][j] == 'B':
                        idx += 1
        cnt.append(min(idx, 64 - idx))

print(min(cnt))