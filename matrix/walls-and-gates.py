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
                    queue.append((r, c, 0))
        
        while queue:
            r, c, count = queue.popleft()
            if rooms[r][c] == -1:
                continue
            elif rooms[r][c] != 0:
                count += 1
            rooms[r][c] = min(count, rooms[r][c])
            for ir, ic in dirs:
                nr = ir + r
                nc = ic + c
                if valid(nr, nc) and rooms[nr][nc] > 10000:
                    queue.append((nr, nc, count))

        return rooms