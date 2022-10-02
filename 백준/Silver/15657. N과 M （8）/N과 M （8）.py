from itertools import combinations_with_replacement
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

array = combinations_with_replacement(num, m)

for i in array:
    for j in i:
        print(j, end=' ')
    print()