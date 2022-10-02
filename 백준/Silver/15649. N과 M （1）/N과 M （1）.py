import sys
from itertools import permutations

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

sequence = list(permutations(range(1, n+1), m))

for i in sequence:
    for j in i:
        print(j, end=' ')
    print()