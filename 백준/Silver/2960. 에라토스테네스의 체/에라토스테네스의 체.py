import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
num = [True] * (n+1)
num[1] = False
cnt = 0

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if num[j] == True:
            num[j] = False
            cnt += 1
            if cnt == k:
                print(j)
                break