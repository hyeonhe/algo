import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0]

for i in range(n):
    prefix_sum.append(prefix_sum[i] + array[i])

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])