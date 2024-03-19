t = int(input())
arr = list(int(input()) for i in range(t))

dp=[0,1,2,4]

for i in range(4, max(arr)+1):
    dp.append((dp[i-1] + dp[i-2] +dp[i-3]) % 1000000009)
    
for i in arr:
    print(dp[i])