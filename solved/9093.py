import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for i in range(t):
    word = input().split()
    for j in word:
        print(j[::-1], end=' ')
    print()