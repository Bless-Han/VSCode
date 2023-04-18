class Road:
    def __init__(self, length = float('inf'), cost = float('inf')):
        self.length = length
        self.cost = cost

def floyd(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j].length < graph[i][k].length + graph[k][j].length or\
                    (graph[i][j].length == )
                    # graph[i][j].length = graph[i][k].length + graph[k][j].length

n, m, s, d = map(int, input().split())
graph = [[Road() for _ in range(n)] for _ in range(n)]
for i in range(n):
    graph[i][i].length = 0
    graph[i][i].cost = 0
for _ in range(m):
    a, b, length, cost = map(int, input().split())
    graph[a][b].length = length
    graph[a][b].cost = cost
    graph[b][a].length = length
    graph[b][a].cost = cost
floyd(graph, n)
for i in range(n):
    for j in range(n):
        print(graph[i][j].length, graph[i][j].cost, " ", end="")
    print()

print(graph[s][d].length, graph[s][d].cost)
