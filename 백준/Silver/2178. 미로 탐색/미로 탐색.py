from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(graph, x, y):
    queue = deque()
    queue.append([x, y])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
        
            if graph[nx][ny] == 1:
                queue.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

            if nx == n - 1 and ny == m - 1:
                break
    
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
print(bfs(graph, 0, 0))