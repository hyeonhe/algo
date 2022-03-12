# https://www.acmicpc.net/problem/21920
n = int(input())
a = list(map(int, input().split()))
x = int(input())

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

ans = []
for i in a:
    if gcd(x, i) == 1:
        ans.append(i)

print(sum(ans) / len(ans))