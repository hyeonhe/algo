import sys
sys.setrecursionlimit(10**7)

def input():
    return sys.stdin.readline().rstrip()

n, m = map(int, input().split())
visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

for array in graph:
    array.sort()

def dfs(graph, visited, v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, visited, i)

    return True

answer = 0
for i in range(1, n + 1):
    if not visited[i]:
        answer += dfs(graph, visited, i)

print(answer)