from itertools import combinations_with_replacement
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = sorted(list(map(int, input().split())))
array = sorted(set(combinations_with_replacement(num, m)))

for i in array:
    print(' '.join(map(str, i)))