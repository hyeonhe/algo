import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
w = []

for i in range(n):
    w.append(list(map(int, input().split())))

w.sort()


for i in range(n):
    print(w[i][0], w[i][1])