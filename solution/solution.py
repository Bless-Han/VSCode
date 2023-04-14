
n, e = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for u in range(n):
    graph[u].sort()
visited = [False] * n
for u in range(n):
    course = []
    dfs(graph, visited, u, course)
    print("{", *course, "}")
visited = [False] * n
for u in range(n):
    course = []
    bfs(graph, visited, u, course)
    print("{", *course, "}")
