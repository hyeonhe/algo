import sys
from math import sqrt

def input():
    return sys.stdin.readline().rstrip()
    
m, n = map(int, input().split())
num = [True] * (n+1)
num[1] = False

for i in range(2, int(sqrt(n+1)) + 1):
    if num[i] == True:
        j = 2
        while i * j <= n:
            num[i * j] = False
            j += 1

for i in range(m, n+1):
    if num[i]:
        print(i)
    