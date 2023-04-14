def main():
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][j] < graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    max_ = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > max_:
                max_ = graph[i][j]
    if max_ == 0:
        print(0)
    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == max_:
                    print(i+1, max_)
                    return

if __name__ == '__main__':
    main()


