class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = {}
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
        def find(r, c):
            if (r, c) in seen:
                return 
            seen[(r, c)] = True
            for ra, ca in dirs:
                nr = ra + r
                nc = ca + c
                if valid(nr, nc) and grid[nr][nc] == "1":
                    find(nr, nc)
            return
        count = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == "1" and (r, c) not in seen:
                    find(r, c)
                    count += 1
        return count