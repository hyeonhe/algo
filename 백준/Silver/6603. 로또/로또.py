from itertools import combinations
import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    num = list(map(int, input().split()))
    if num[0] == 0:
        break

    num = num[1:]
    case = list(combinations(num, 6))

    for i in case:
        for j in i:
            print(j, end=' ')
        print()
    print()