import sys

def input():
    return sys.stdin.readline().rstrip()

n  = int(input())
arr = [0] + [int(input()) for _ in range(n)]

dp = [0]
dp.append(arr[1])
if n > 1:
    dp.append(arr[1] + arr[2])

for i in range(3, n+1):
    dp.append(max(arr[i] + arr[i-1] + dp[i-3], dp[i-1], arr[i] + dp[i-2]))

print(dp[n])