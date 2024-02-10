import sys
from collections import deque

def input():
    return sys.stdin.readline().rstrip()

dx = [1,-1,0,0]
dy = [0,0,1,-1]

a, b = map(int, input().split())

graph = []
x, y = 0, 0
cnt = 0
for i in range(a):
    arr = list(input())
    graph.append(arr)
    if 'I' in arr:
        x = i
        y = arr.index('I')
        
        
        
def bfs(x, y):
    queue = deque()
    cnt = 0
    queue.append((x,y))
    graph[x][y] = 'X'
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= a or ny < 0 or ny >= b:
                continue
            if graph[nx][ny] == 'X':
                continue
            elif graph[nx][ny] == 'O' or graph[nx][ny] == 'P':
                if graph[nx][ny] == 'P':
                    cnt += 1
                graph[nx][ny] = 'X' 
                queue.append((nx, ny))

    return cnt if cnt > 0 else 'TT'

print(bfs(x, y))