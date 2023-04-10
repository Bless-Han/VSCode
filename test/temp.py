"""
7-6 列出连通集
分数 25
作者 陈越
单位 浙江大学
给定一个有N个顶点和E条边的无向图，请用DFS和BFS分别列出其所有的连通集。假设顶点从0到N−1编号。进行搜索时，假设我们总是从编号最小的顶点出发，按编号递增的顺序访问邻接点。

输入格式:
输入第1行给出2个整数N(0<N≤10)和E，分别是图的顶点数和边数。随后E行，每行给出一条边的两个端点。每行中的数字之间用1空格分隔。

输出格式:
按照"{ v 
1
​
  v 
2
​
  ... v 
k
​
  }"的格式，每行输出一个连通集。先输出DFS的结果，再输出BFS的结果。

输入样例:
8 6
0 7
0 1
2 0
4 1
2 4
3 5
输出样例: { 0 1 4 2 7 } { 3 5 }
{ 6 }
{ 0 1 2 7 4 }
{ 3 5 }
{ 6 }
代码长度限制
16 KB
时间限制
400 ms
内存限制
64 MB
"""
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
            dfs(graph, visited, i)
    print()
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            bfs(graph, visited, i)
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
    ...
def bfs(graph, visited, u):
    global course
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        course.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
if __name__ == '__main__':
    main() course = []
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
    ...
def bfs(graph, visited, u):
    global course
    queue = [u]
    visited[u] = True
    while queue:
        u = queue.pop(0)
        course.append(u)
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
if __name__ == '__main__':
    ma