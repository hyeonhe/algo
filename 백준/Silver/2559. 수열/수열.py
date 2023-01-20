import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
array = list(map(int, input().split()))
first = sum(array[:k])
ans_array = [first]

ans = -101
for i in range(1, n-k+1):
    ans_array.append(ans_array[i-1] - array[i-1] + array[i+k-1])

print(max(ans_array))