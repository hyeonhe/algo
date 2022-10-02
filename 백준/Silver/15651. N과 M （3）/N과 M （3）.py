import sys
from itertools import product

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())

sequence = list(product(range(1, n+1), repeat = m))

for i in sequence:
    for j in i:
        print(j, end=' ')
    print()