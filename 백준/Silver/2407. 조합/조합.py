import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

answer = 1
for i in range(1, k+1):
    answer *= n
    n -= 1
    answer //= i

print(answer)