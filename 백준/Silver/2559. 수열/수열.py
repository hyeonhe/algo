import sys
def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
array = list(map(int, input().split()))
first = sum(array[:k])
ans_array = [first]

for i in range(n-k):
    ans_array.append(ans_array[i] - array[i] + array[i+k])

print(max(ans_array))