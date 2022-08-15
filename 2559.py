import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
array = list(map(int, input().split()))

sum_arr = []

for i in range(n-1):
    sum_arr.append(sum(array[i:i+k]))

print(max(sum_arr))