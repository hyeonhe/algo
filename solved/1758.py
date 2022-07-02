import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

array = [int(input()) for i in range(n)]
array.sort(reverse=True)

result = 0

for i in range(n):
    if array[i] - i > 0:
        result += array[i] - i

print(result)