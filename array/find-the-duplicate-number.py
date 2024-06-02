class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slowN = 0
        while True:
            slowN = nums[slowN]
            slow = nums[slow]
            if slowN == slow:
                return slow
        