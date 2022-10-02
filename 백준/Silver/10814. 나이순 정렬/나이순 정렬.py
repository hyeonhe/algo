import sys

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
name = []

for i in range(n):
    data = input().split()
    name.append([int(data[0]), data[1]])

name.sort(key=lambda x: x[0])

for i in range(n):
    print(name[i][0], name[i][1])