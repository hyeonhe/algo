import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

array = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def bfs(graph, a, b):
    queue = deque()
    graph[a][b] = 0
    queue.append((a, b))
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1

    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            array.append(bfs(graph, i, j))
            
array.sort()
print(len(array))

for i in array:
    print(i)