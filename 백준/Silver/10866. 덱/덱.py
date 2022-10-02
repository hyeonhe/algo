import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n = int(input())
deque = deque()
com = []

for i in range(n):
    com = input().split()
    if com[0] == 'push_front':
        deque.appendleft(com[1])
    elif com[0] == 'push_back':
        deque.append(com[1])
    elif com[0] == 'pop_front':
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif com[0] == 'pop_back':
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif com[0] == 'size':
        print(len(deque))
    elif com[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif com[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif com[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)