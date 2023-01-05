import sys

def input():
    return sys.stdin.readline().rstrip()
 
a, b = map(int, input().split())
cnt = 1

while b != a:
    temp = b

    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    cnt += 1

    if temp == b:
        print(-1)
        break
else:
    print(cnt)