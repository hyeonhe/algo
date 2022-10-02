import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
array = list(map(int, input().split()))

array.sort()

print(array[(n-1) // 2])