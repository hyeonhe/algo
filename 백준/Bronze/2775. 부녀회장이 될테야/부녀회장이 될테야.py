import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

array = [[] for i in range(15)]

for i in range(15):
    for j in range(14):
        if i == 0:
            array[i].append(j+1)
        else:
            array[i].append(sum(array[i-1][:j+1]))

for _ in range(t):
    k = int(input())
    n = int(input())
    
    print(array[k][n-1])