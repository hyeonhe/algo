import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())

array = [0, 1, 2]

for i in range(3, n+1):
    array.append(array[i-1] + array[i-2])

print(array[n] % 10007)