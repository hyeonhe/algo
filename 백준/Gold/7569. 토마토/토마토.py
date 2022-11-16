import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for j in range(n)] for i in range(h)]

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
queue = deque()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k] == 1:
                queue.append((i, j, k))

def bfs():
    while queue:
        x, y, z = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if nx < 0 or nx >= h or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if graph[nx][ny][nz] == 0:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                queue.append((nx, ny, nz))

bfs()
# print(graph[0])
# print(graph[1])

result = 0
for i in graph:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                quit(0)
        result = max(result, max(j))

print(result - 1)