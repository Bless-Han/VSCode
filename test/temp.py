class Solution:
    def bfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        queue = collections.deque([(i, j)])
        visited.add((i, j))
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == "1" and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in visited:
                    res += 1
                    self.bfs(grid, i, j, visited)
        return res