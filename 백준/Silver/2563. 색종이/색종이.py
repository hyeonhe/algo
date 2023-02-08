import sys
input = sys.stdin.readline

n = int(input())
array = [[0] * 101 for _ in range(101)]
ans = 0

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(x, x + 10):
        for j in range(y, y + 10):
            array[i][j] = 1

for a in array:
    ans += sum(a)

print(ans)