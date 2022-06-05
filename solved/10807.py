import sys 

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
a = list(map(int, input().split()))
v = int(input())

print(a.count(v))