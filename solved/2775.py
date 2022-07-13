import sys

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

# 0층부터 14층
array = [[] for i in range(15)]

for i in range(15):
    for j in range(1, 15):
        if i == 0:
            array[i].append(j)
        else:
            array[i].append(sum(array[i-1][:j]))

for _ in range(t):
    k = int(input())
    n = int(input())
    
    print(array[k][n-1])