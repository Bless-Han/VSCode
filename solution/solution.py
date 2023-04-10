def main():
    n, e = map(int, input().split())
    graph = [[] for _ in range(n)]
    for _ in range(e):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(n):
        graph[i].sort()
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            print("{ ", end="")
            dfs(graph, visited, i)
            print("}")
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            print("{ ", end="")
            bfs(graph, visited, i)
            print("}")
def dfs(graph, visited, u):
    visited[u] = True
    print(u, end=' ')
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)
def bfs(graph, visited, u):
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        print(u, end=' ')
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
if __name__ == '__main__':
    main()
