import sys

def input():
    return sys.stdin.readline().rstrip()

k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]
start = 1
end = max(array)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for i in array:
        cnt += i // mid
    
    if cnt >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)