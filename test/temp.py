class Solution:
    def __init__(self):
        self.directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        self.grid = None
        self.m = None
        self.n = None
        self.visited = None
        self.res = None

    def dfs(self, i, j):
        self.visited[i][j] = True
        for d in self.directions:
            new_i = i + d[0]
            new_j = j + d[1]
            if 0 <= new_i < self.m and 0 <= new_j < self.n and not self.visited[new_i][new_j] and self.grid[new_i][new_j] == '1':
                self.dfs(new_i, new_j)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.m = len(grid)
        self.n = len(grid[0])
        self.visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.res = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.grid[i][j] == '1':
                    self.res += 1
                    self.dfs(i, j)
        return self.res