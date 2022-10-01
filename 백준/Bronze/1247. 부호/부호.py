import sys


def input():
    return sys.stdin.readline().rstrip()


for _ in range(3):
    n = int(input())
    answer = [int(input()) for _ in range(n)]
    if sum(answer) == 0:
        print("0")
    elif sum(answer) > 0:
        print('+')
    else:
        print('-')
