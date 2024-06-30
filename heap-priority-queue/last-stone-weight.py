import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            heavy1 = heapq.heappop(stones)
            heavy2 = heapq.heappop(stones)
            if heavy1 == heavy2:
                continue
            else:
                heavy1 = -1 * abs(heavy1-heavy2)
                heapq.heappush(stones, heavy1)
        if len(stones) == 0:
            return 0
        return -1*stones[0]
            
            