import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

t = int(input())
queue = deque()

for _ in range(t):
    str = input()
    for i in str:
        if i == '(':
            queue.append(i)
        elif i == ')':
            if queue and queue[-1] == '(':
                queue.pop()
            else:
                queue.append(i)
                break
    if queue:
        print('NO')
    else:    
        print('YES')
    queue = []