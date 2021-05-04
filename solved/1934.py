def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


ans = 1
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = gcd(a, b)
    a //= c
    b //= c
    ans = a * b * c
    print(ans)
