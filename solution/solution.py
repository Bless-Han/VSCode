
def floyd(graph, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

n, m = map(int, input().split())
graph = [[float('inf')] * (n + 1) for _ in range(n+1)]
for _ in range(m):
    a, b, val = map(int, input().split())
    graph[a][b] = graph[b][a] = val
for i in range(1, n + 1):
    graph[i][i] = 0
floyd(graph, n)
ans = float('inf')
for i in range(1, n + 1):
    max = 0
    for j in range(1, n + 1):
        if max < graph[i][j]:
            max = graph[i][j]
    if ans > max:
        ans = max
        x = i
if ans == float('inf'):
    print("0")
else:
    print(x, ans)
