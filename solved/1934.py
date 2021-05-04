# t = int(input())

# for i in range(t):
#     a, b = map(int, input().split())
#     largeNum = max([a, b])
#     ans = 1

#     for j in range(1, largeNum + 1):
#         while j <= largeNum:
#             if a % j == 0 and b % j == 0:
#                 ans *= j
#                 a //= j
#                 b //= j
#                 ans = ans * a * b
#             else:
#                 ans = a * b
#     print(ans)

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
