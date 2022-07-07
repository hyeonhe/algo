import sys
from itertools import combinations

def input():
    return sys.stdin.readline().rstrip()

l, c = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()

array = list(combinations(alphabet, l))

for i in array:
    cnt = 0
    for j in i:
        if j in 'aeiou':
            cnt += 1
    if cnt == 0 or l - cnt < 2:
        continue

    print(''.join(i))