# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        c1 = l1
        c2 = l2
        add = 0
        dummy = ListNode()
        head = dummy
        
        while c1 != None and c2 != None:
            head.next = ListNode()
            head = head.next
            s = c1.val + c2.val + add
            add = s // 10
            head.val = s % 10
            print(s, add, head.val)
            c1 = c1.next
            c2 = c2.next
        rest = c1
        if c1 == None:
            rest = c2
        while rest != None:
            head.next = ListNode()
            head = head.next
            s = add + rest.val
            add = s // 10
            head.val = s % 10
            rest = rest.next
        if add != 0:
            head.next = ListNode()
            head = head.next
            head.val = add
        head = None
        return dummy.next






#         def convert (head):
#             i = 0
#             cur = head
#             n = 0
#             while cur != None:
#                 n += cur.val * (10**i)
#                 cur = cur.next
#                 i += 1
#             return n
#         n1 = convert(l1)
#         n2 = convert(l2)
#         s = n1 + n2
#         ans = ListNode(-1)
#         new = ans
#         if s == 0:
#             return ListNode(0)
#         while s>0:
#             new.next = ListNode(s%10)
#             new = new.next
#             s //= 10
#         return ans.next

#     # def help (l):
#     #     num = 0
#     #     for i in range (len(l)):
#     #         if i == 0: num+=l[i]
#     #         else: num+= l[i]*pow(10,i)
#     #     return num
#     # def addTwoNumbers(self, l1, l2):
#     #     """
#     #     :type l1: ListNode
#     #     :type l2: ListNode
#     #     :rtype: ListNode
#     #     """
#     #     newl1 = help(l1)
#     #     newl2 = help(l2)
#     #     new = newl1 + newl2
#     #     newL= []
#     #     while new>0:
#     #         newL.append (new%10)
#     #         new = new//10
#     #     return newL
















# # newList = []
# #         bigger = l1 if (len(l1) > len(l2)) else l2
# #         smaller = l1 if (len(l1) < len(l2)) else l2
# #         toAdd = 0
# #         for i in range(len(smaller)):
# #             sum = l1[i] + l2[i]
# #             newList.append(i+toAdd)
# #             toAdd = sum / 10
# #         if toAdd > 0: newList.append(bigger[len(smaller)+toAdd])
# #         return newList+bigger[len(smaller)+1::]
        