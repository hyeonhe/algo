import sys

def input():
    return sys.stdin.readline().rstrip()

def gcd(x, y):
        
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())
s = list(map(int, input().split()))

s.sort()
ans = gcd(s[1], gcd(s[-1], s[0]))

for i in range(1, (ans // 2) + 1):
    if ans % i == 0:
        print(i)

print(ans)