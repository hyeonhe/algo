import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = {}

for i in range(1, n+1):
    p = input()
    array[i] = p
    array[p] = i

for i in range(m):
    p = input()
    if p.isdigit():
        print(array[int(p)])
    else:
        print(array[p])
