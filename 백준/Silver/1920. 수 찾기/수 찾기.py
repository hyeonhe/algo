import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

def search(array, start, end, target):
    mid = (start + end) // 2
    while start <= end:
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
            return search(array, start, end, target)
        elif array[mid] < target:
            start = mid + 1
            return search(array, start, end, target)
        
    return 0

for i in range(m):
    print(search(a, 0, n-1, b[i]))