from collections import deque
import sys

def input():
    return sys.stdin.readline().rstrip()

n, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
S, X, Y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

queue = []
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            queue.append((graph[i][j], i, j))
queue.sort()

def bfs():
    q = deque(queue)
    cnt = 0
    while q:
        if cnt == S:
            break

        for _ in range(len(q)):
            num, x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y]
                    q.append((num, nx, ny))

        cnt += 1

    return graph[X-1][Y-1]

print(bfs())