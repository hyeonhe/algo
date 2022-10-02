a, b = map(int, input().split())
c = int(input())

if a + b < 2 * c:
    print(a + b)
elif a + b >= 2 * c:
    print(a + b - 2 * c)