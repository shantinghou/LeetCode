class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        def valid(r, c):
            return r >= 0 and c >= 0 and r < len(rooms) and c < len(rooms[0])
        
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        for r in range(len(rooms)):
            for c in range(len(rooms[r])):
                if rooms[r][c] == 0:
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            if rooms[r][c] == -1:
                continue
            for ir, ic in dirs:
                nr = ir + r
                nc = ic + c
                if valid(nr, nc) and rooms[nr][nc] == 0:
                    continue
                if valid(nr, nc) and rooms[nr][nc] > 10000000:
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))

        return rooms