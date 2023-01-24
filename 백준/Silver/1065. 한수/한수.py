n = int(input())
ans = 0

if n < 100:
    ans = n
else:
    ans = 99

for i in range(100, n+1):
    num = str(i)
    a, b, c = int(num[0]), int(num[1]), int(num[2])
    if c - b == b - a:
        ans += 1

print(ans)