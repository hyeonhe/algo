import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
array = [int(input()) for i in range(n)]
dp = [0] * (n + 1)

# print(array)
dp[1] = array[0]
dp[2] = dp[1] + array[1]
# dp[3] = max(dp[2], array[0] + array[2])

for i in range(3, n+1):
    dp[i] = max(array[i-1] + dp[i-2], dp[i-1], dp[i-3] + array[i-2]  + array[i-1])


print(dp[-1])