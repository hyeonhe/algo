import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, -1, 1, -1, 1]
q = deque()

def bfs(x, y):
    q.append((x, y))

    while q:
        x, y = q.popleft()
        graph[x][y] = 0

        for i in range(8):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)