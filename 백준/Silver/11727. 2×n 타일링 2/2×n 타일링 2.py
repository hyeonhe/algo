import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

array = [0, 1, 3]

for i in range(3, n+1):
    array.append(array[i-2] * 2 + array[i-1])

print(array[n] % 10007)