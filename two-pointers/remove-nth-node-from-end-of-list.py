# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        cur = head
        while cur != None:
            cur = cur.next
            length += 1
        n = length - n
        count = 0
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        while cur != None and cur.next != None:
            if count == n:
                cur.next = cur.next.next
            else:
                cur = cur.next
            count += 1
        return dummy.next
