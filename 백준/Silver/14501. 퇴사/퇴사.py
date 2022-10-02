n = int(input())
t = []
p = []
dp = [0] * (n + 1)

for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

max_value = 0
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(max_value, p[i] + dp[time])
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)