import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
coin = set([int(input()) for i in range(n)])

dp = [0] * (k + 1)
for i in range(1, k + 1):
    arr = []
    for c in coin:
        if i-c >= 0 and dp[i-c] >= 0:
            arr.append(dp[i-c])
    if arr:
        dp[i] = min(arr) + 1
    else:
        dp[i] = -1

print(dp[k])