import sys

def input():
    return sys.stdin.readline().rstrip()
    
t = int(input())

for _ in range(t):
    array = list(map(int, input().split()))
    array.sort()
    print(array[-3])