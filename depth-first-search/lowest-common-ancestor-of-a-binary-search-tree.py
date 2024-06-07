# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(root):
            if root == None:
                return (None, False, False)

            (loc, pf, qf) = find(root.left)
            (loc1, pf1, qf1) = find(root.right)
            
            if loc != None:
                return (loc, pf, qf)
            if loc1 != None:
                return (loc1, pf1, qf1)

            pres = pf or pf1
            qres = qf or qf1

            if root == p:
                pres = True
            elif root == q:
                qres = True

            if pres and qres:
                return (root, True, True)
            return (None, pres, qres)
        l, p, q = find(root)
        return l
        