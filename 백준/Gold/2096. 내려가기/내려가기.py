import sys

def input():
    return sys.stdin.readline().rstrip()

dp1 = [0] * 3
dp2 = [0] * 3
dp1_tmp = [0] * 3
dp2_tmp = [0] * 3

n = int(input())

for i in range(n):
    a, b, c = map(int, input().split())

    for j in range(3):
        if j == 0:
            dp1_tmp[j] = a + max(dp1[j], dp1[j+1])
            dp2_tmp[j] = a + min(dp2[j], dp2[j+1])
        elif j == 1:
            dp1_tmp[j] = b + max(dp1[j], dp1[j-1], dp1[j+1])
            dp2_tmp[j] = b + min(dp2[j], dp2[j-1], dp2[j+1])
        else:
            dp1_tmp[j] = c + max(dp1[j], dp1[j-1])
            dp2_tmp[j] = c + min(dp2[j], dp2[j-1])

    for j in range(3):
        dp1[j] = dp1_tmp[j]
        dp2[j] = dp2_tmp[j]

print(max(dp1), min(dp2))