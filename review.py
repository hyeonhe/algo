# 5430
import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

t = int(input())

for i in range(t):
    command = list(input())
    n = int(input())
    array = []
    a = list(input()[1:-1].split(','))
    
    for j in a:
        try:
            array.append(int(j))
        except ValueError:
            print('error')
            exit(0)


    for c in command:
        if c == 'R':
            