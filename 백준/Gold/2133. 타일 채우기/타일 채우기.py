n = int(input())

dp = [0] * 31
dp[2] = 3
dp[4] = 11

for i in range(6, 31, 2):
    dp[i] = dp[i-2] * 3 + sum(dp[:i-3]) * 2 + 2

print(dp[n])