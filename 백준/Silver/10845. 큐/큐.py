import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()

for i in range(n):
    com = sys.stdin.readline().rstrip()
    if com == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif com == 'size':
        print(len(queue))
    elif com == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif com == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif com == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        x = int(com[5:])
        queue.append(x)