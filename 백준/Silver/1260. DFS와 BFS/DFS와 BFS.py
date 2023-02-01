import sys
from collections import deque
input = sys.stdin.readline
n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
q = deque()

def dfs(v):
    visited[v] = 1
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

def bfs(v):
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

dfs(v)
print()

visited = [0] * (n + 1)
bfs(v)