from itertools import product
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))

array = sorted(set(product(num, repeat = m)))

for i in array:
    print(' '.join(map(str, i)))