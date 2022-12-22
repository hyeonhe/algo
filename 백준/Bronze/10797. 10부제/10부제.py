import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
arr = list(map(int, input().split()))
print(arr.count(n))