class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
        maxCount = 0
        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0])
        while queue:
            r, c, count = queue.popleft()
            for ir, ic in dirs:
                nr = r + ir
                nc = c + ic
                if valid(nr, nc) and grid[nr][nc] == 1:
                    grid[nr][nc] += 1
                    queue.append((nr, nc, count + 1))
            maxCount = max(maxCount, count)
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    return -1
        return maxCount
            
        