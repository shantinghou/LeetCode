"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dummy = Node(0)
        copy = dummy
        cur = head
    
        dicCloned = {}
        while cur != None:
            copy.next = Node(cur.val, None, None)
            copy = copy.next
            dicCloned[cur] = copy
            cur = cur.next
        cur = head
        copy = dummy.next

        while cur != None:
            if cur.random != None:
                copy.random = dicCloned[cur.random]
            cur = cur.next
            copy = copy.next
        return dummy.next