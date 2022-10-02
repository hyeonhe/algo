def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)


def lcm(x, y):
    ans = 1
    z = gcd(x, y)
    x //= z
    y //= z
    ans = x * y * z
    return ans


a, b = map(int, input().split())
print(gcd(a, b))
print(lcm(a, b))