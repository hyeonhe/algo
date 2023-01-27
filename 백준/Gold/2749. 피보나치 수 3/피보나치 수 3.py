import sys
input = sys.stdin.readline

n = int(input())

dp = [0, 1]
mod = 1000000
p = 1500000

for i in range(2, p):
    dp.append((dp[i - 2] + dp[i - 1]) % mod)

print(dp[n % p])