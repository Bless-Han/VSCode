def dfs(graph, visited, u, course):
    visited[u] = True
    course.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v, course)

def bfs(graph, visited, u, course):
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        course.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

n, e = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for i in range(n):
    graph[i].sort()
visited = [False] * n
for u in range(n):
    if not visited[u]:
        course = []
        dfs(graph, visited, u, course)
        print("{", *course, "}")
visited = [False] * n
for u in range(n):
    if not visited[u]:
        course = []
        bfs(graph, visited, u, course)
        print("{", *course, "}")
