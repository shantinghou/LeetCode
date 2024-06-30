from heapq import heapify, heappush, heappop 
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.larger = nums
        heapify(self.larger)
        self.smaller = []
        heapify(self.smaller)
        while len(self.larger) > self.k:
            heappush(self.smaller, heappop(self.larger))

    def add(self, val: int) -> int:
        if len(self.larger) < self.k:
            heappush(self.larger, val)
        elif self.larger[0] <= val:
            heappush(self.larger, val)
            heappush(self.smaller, heappop(self.larger))
        else:
            heappush(self.smaller, val)
        return self.larger[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)