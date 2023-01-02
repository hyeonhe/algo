import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = [list(input()) for _ in range(n)]
cnt = []

for a in range(n - 7):
    for b in range(m - 7):
        idx1 = 0
        idx2 = 0

        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if array[i][j] == 'W':
                        idx1 += 1
                    else:
                        idx2 += 1
                else:
                    if array[i][j] == 'B':
                        idx1 += 1
                    else:
                        idx2 += 1
        cnt.append(min(idx1, idx2))

print(min(cnt))