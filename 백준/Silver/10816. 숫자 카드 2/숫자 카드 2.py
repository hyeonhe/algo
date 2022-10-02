import sys
from collections import Counter

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
card = list(map(int, input().split()))
m = int(input())
array = list(map(int, input().split()))

card_count = Counter(card)

for i in array:
    print(card_count[i], end=' ')