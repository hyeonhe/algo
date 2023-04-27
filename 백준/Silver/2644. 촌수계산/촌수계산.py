from collections import deque
graph = [[] for i in range(101)]

n = int(input())
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [0] * 101

cnt = 0
def bfs(start):
    queue = deque([start])

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = visited[x] + 1

bfs(a)
print(visited[b] if visited[b] > 0 else -1)