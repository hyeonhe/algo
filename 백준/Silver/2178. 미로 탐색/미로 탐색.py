from collections import deque
import sys
def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
array = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    row = list(input())
    array.append(row)

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    array[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] == '1':
                queue.append((nx, ny))
                array[nx][ny] = array[x][y] + 1
            
            if nx == n - 1 and ny == m - 1:
                break
    return array[n-1][m-1]

print(bfs(0, 0))