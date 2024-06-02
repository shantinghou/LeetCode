# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = None
        # cur = head
        # while cur != None:
        #     temp = cur
        #     cur = cur.next
        #     temp.next = prev
        #     prev = temp
        # return prev




        last = head
        if last == None:
            return last
        cur = head.next
        last.next = None

        while cur != None:
            temp = cur
            cur = cur.next
            temp.next = last
            last = temp
        return last