# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find med
        med = fast = head
        while fast and fast.next:
            med = med.next
            fast = fast.next.next
        # reverse
        last = med
        cur = last.next
        last.next = None
        while cur != None:
            temp = cur
            cur = cur.next
            temp.next = last
            last = temp
        print(last)
        # combine
        front = head
        back = last
        while back.next:
            front.next, front = back, front.next
            back.next, back = front, back.next
        return head