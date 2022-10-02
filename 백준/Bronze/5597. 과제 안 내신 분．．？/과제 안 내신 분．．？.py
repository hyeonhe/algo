import sys

def input():
    return sys.stdin.readline().rstrip()

s = [i for i in range(1, 31)]

for i in range(28):
    s.remove(int(input()))

for i in s:
    print(i)