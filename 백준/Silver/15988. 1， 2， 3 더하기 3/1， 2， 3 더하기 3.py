import sys
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
arr = list(int(input()) for _ in range(t))

dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 1000001):
    dp[i] = ((dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009)
    
for i in arr:
    print(dp[i])