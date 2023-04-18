from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for j in range(m)] for i in range(n)]
    ans = bfs(0, 0, n, m, maps, visited)
    
    return ans if ans != 1 else -1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y, n, m, maps, visited):
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny]:
                q.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
                visited[nx][ny] = 1
                
                
    return maps[n-1][m-1]