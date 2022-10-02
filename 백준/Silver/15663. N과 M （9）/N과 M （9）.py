from itertools import permutations
import sys

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
a = list(map(int, input().split()))

array = permutations(a, m)
array = list(set(array))
array.sort()

for i in array:
    for j in i:
        print(j, end=' ')
    print()