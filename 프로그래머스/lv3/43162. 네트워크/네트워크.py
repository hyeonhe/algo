from collections import deque
def solution(n, computers):
    visited = [False] * n
    # graph = [[] for i in range(n + 1)]
    # for i in range(n):
    #     for j in range(n):
    #         if i == j:
    #             continue
    #         elif computers[i][j] == 1:
    #             graph[i+1].append(j+1)
                
    answer = 0
    
    for i in range(n):
        if not visited[i]:
            answer += bfs(visited, computers, i)
    return answer

def bfs(visited, graph, start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in range(len(graph)):
            if not visited[i] and v != i and graph[v][i] == 1:
                queue.append(i)
                visited[i] = True
                
    return 1