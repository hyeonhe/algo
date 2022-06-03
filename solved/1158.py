import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())
queue = deque([i + 1 for i in range(n)])

save = []

while queue:
    queue.rotate(-k)
    save.append(queue.pop())

print('<' + ', '.join(map(str, save)) + '>')