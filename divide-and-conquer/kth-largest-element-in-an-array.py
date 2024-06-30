import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-1*n for n in nums]
        heapq.heapify(nums)
        count = 1
        while count < k:
            heapq.heappop(nums)
            count += 1
        return -1*heapq.heappop(nums)