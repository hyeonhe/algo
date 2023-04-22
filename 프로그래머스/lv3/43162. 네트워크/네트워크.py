from collections import deque
def solution(n, computers):
    visited = [False] * (n + 1)
    graph = [[] for i in range(n + 1)]
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            elif computers[i][j] == 1:
                graph[i+1].append(j+1)
                
    answer = 0
    
    for i in range(1, n + 1):
        if not visited[i]:
            answer += bfs(visited, graph, i)
    return answer

def bfs(visited, graph, start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
    return 1