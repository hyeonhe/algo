import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = list(map(int, input().split()))
prefix_sum = [0]
sum = 0

for i in array:
    sum += i
    prefix_sum.append(sum)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])