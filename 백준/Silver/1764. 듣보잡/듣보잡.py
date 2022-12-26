import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

a = set(input() for _ in range(n))
b = set(input() for _ in range(m))

arr = sorted(a.intersection(b))
print(len(arr))
print('\n'.join(arr))