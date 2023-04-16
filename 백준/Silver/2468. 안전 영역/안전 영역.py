from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

n = int(input())
graph = []
max_num = 0

for i in range(n):
    graph.append(list(map(int, input().split())))
    max_num = max(max_num, max(graph[i]))

dx = [0 ,0, 1, -1]
dy = [1, -1, 0 ,0]
def bfs(value, x, y, visited):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()
        visited[x][y] = 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] > value and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
    return 1

ans = 0
for i in range(max_num):
    cnt = 0
    visited = [[0] * n for i in range(n)]

    for j in range(n):
        for k in range(n):
            if graph[j][k] > i and visited[j][k] == 0:
                cnt += bfs(i, j, k, visited)

    if ans < cnt:
        ans = cnt

print(ans)