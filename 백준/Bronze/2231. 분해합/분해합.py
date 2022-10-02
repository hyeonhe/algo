import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

ans = 0
for i in range(1, n+1):
    ans += i
    i = str(i)
    for j in i:
        ans += int(j)

    if ans == n:
        print(i)
        break
    
    ans = 0

if ans == 0:
    print(ans)