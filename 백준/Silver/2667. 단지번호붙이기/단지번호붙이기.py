from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] += 1
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

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

total = 0
arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            total += 1
            arr.append(bfs(i, j))

arr.sort()
print(total)
print('\n'.join(map(str, arr)))