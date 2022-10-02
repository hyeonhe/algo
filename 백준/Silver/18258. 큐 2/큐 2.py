import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()


for i in range(n):
    command = sys.stdin.readline().rstrip()
    length = len(queue)
    if command == 'pop':
        if length == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':
        if length == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':
        if length == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':
        if length == 0:
            print(-1)
        else:
            print(queue[-1])
    else:
        x = int(command[5:])
        queue.append(x)