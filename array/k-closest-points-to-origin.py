import math, heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x1, y1):
            return math.sqrt((x1 - 0)**2 + (y1 - 0)**2)
        closest = []
        heapq.heapify(closest)
        for p in points:
            heapq.heappush(closest, (dist(p[0], p[1]), p[0], p[1]))
        res = []
        count = 0
        while count < k:
            ans = heapq.heappop(closest)
            res.append([ans[1], ans[2]])
            count += 1
        return res
        