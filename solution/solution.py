def bfs(graph, visited, u):
    queue = [u]
    visited[u] = True
    level = 0
    while queue:
        u = queue.pop(0)
        for v in graph[u]:
            queue.append(v)
            visited[v] = True
            if v == graph[u][-1]:
                level += 1
        if level > 6:
            break

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for u in range(1, n+1):
    visited = [False] * (n + 1)
    bfs(graph, visited, u)
    print(f"{u}: {sum(visited)*100/n:.2f}%")


