# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        cur = head
        i = 0
        while cur != None:
            if cur in seen:
                return True
            seen[cur] = i
            i += 1
            cur = cur.next
        return False









        # seen = {}
        # p = head
        
        # while p != None:
        #     if p in seen:
        #         return True
        #     seen[p] = True
        #     p = p.next
        # return False