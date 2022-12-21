from itertools import product
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

array = product(num, repeat = m)

print('\n'.join(' '.join(map(str, i)) for i in array))