n = int(input())
ans = 0

if n < 100:
    ans = n
else:
    ans = 99

for i in range(100, n+1):
    if (i // 100) + (i % 10) == 2 * (i // 10 % 10):
        ans += 1

print(ans)