import sys
from itertools import combinations_with_replacement

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

sequence = list(combinations_with_replacement(range(1, n+1), m))

for i in sequence:
    for j in i:
        print(j, end=' ')
    print()