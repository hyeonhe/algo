import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip()

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

n = int(input())

for _ in range(n):
    num = list(map(int, input().split()))
    array = list(combinations(num[1:], 2))
    ans = 0
    for i in array:
        ans += gcd(i[0], i[1])

    print(ans)