
from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
    return

t = int(input())

for _ in range(t):
    cnt = 0
    n, m, k = map(int, input().split())
    array = [[0] * m for _ in range(n)]

    for _ in range(k):
        a, b = map(int, input().split())
        array[a][b] = 1

    for a in range(n):
        for b in range(m):
            if array[a][b] == 1:
                bfs(array, a, b)
                cnt += 1

    print(cnt)