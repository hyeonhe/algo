import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

front = deque(input())
back = deque()

n = int(input())
for _ in range(n):
    command = list(input().split())
    if command[0] == 'P':
        front.append(command[1])
    elif command[0] == 'L' and len(front) > 0:
        back.appendleft(front.pop())
    elif command[0] == 'D' and len(back) > 0:
        front.append(back.popleft())
    elif command[0] == 'B':
        if len(front) > 0:
            front.pop()

print(''.join(front + back))