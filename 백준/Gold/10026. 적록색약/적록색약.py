from collections import deque
import sys
def input():
  return sys.stdin.readline().rstrip()

n = int(input())
graph = [list((input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(c, x, y):
  queue = deque()
  queue.append((x, y))
  visited[x][y] = 1

  while queue:
    x, y = queue.popleft()
    if graph[x][y] == 'R':
          graph[x][y] ='G'

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= n or ny < 0 or ny >= n:
        continue

      if visited[nx][ny] == 0 and graph[nx][ny] == c:
        visited[nx][ny] = 1
        queue.append((nx, ny))

  return 1


cnt1 = 0
cnt2 = 0

visited = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      cnt1 += bfs(graph[i][j], i, j)

visited = [[0 for i in range(n)] for _ in range(n)]
for i in range(n):
  for j in range(n):
    if visited[i][j] == 0:
      cnt2 += bfs(graph[i][j], i, j)

print(cnt1, cnt2)