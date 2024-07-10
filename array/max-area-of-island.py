class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = {}
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
        def dfs(r, c):
            if (r, c) in seen:
                return 0
            seen[(r, c)] = True
            total = 1
            for ra, ca in dirs:
                nr = ra + r
                nc = ca + c
                if valid(nr, nc) and grid[nr][nc] == 1:
                    total += dfs(nr, nc)
            return total
        maximum = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1 and (r, c) not in seen:
                    maximum = max(maximum, dfs(r, c))
        return maximum