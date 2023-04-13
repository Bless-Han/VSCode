def dfs(graph, visited, u, layer):
    if layer > 6:
        return
    visited[u] = True


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for u in range(1, n+1):
    visited = [False] * (n + 1)
    dfs(graph, visited, u, 1)
    print(f"{u}: {sum(visited)/n*100:.0f}%")
