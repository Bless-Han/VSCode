def floyd(d, n):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

def main():
    n, m = map(int, input().split())
    d = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        d[i][i] = 0
    for _ in range(m):
        x, y, z = map(int, input().split())
        d[x][y] = z
        d[y][x] = z
    for e in d:
        print(e)
    floyd(d, n)
    for e in d:
        print(e)
    ans = float('inf')
    for i in range(1, n + 1):
        max = 0
        for j in range(1, n + 1):
            if i != j and d[i][j] < ans:
                ans = d[i][j]
                x = i
    if ans == float('inf'):
        print(0)
    else:
        print(x, ans)

if __name__ == '__main__':
    main()
