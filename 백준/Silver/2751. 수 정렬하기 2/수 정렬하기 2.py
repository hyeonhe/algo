import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

array = []
for _ in range(n):
    array.append(int(input()))

array.sort()

for i in array:
    print(i)