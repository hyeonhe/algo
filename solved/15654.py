# 순열
from itertools import permutations
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
num = list(map(int, input().split()))
num.sort()

array = permutations(num, m)

for i in array:
    for j in i:
        print(j, end=' ')
    print()