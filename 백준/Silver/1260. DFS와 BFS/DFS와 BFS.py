import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(len(graph)):
  graph[i].sort()

def dfs(graph, v, visited):
  visited[v] = 1
  print(v, end = ' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)

def bfs(graph, v, visited):
  visited[v] = 1
  queue = deque([v])

  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = 1

dfs(graph, v, visited)
print()

visited = [0] * (n + 1)

bfs(graph, v, visited)