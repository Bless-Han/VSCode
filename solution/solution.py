course = []
def main():
    global course
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
            course = []
            dfs(graph, visited, i)
            print("{", *course, "}")
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            course = []
            bfs(graph, visited, i)
            print("{", *course, "}")
def dfs(graph, visited, u):
    global course
    visited[u] = True
    course.append(u)
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)





















def bfs(graph, visited, u):
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        course.append(u)

if __name__ == '__main__':
    main()
