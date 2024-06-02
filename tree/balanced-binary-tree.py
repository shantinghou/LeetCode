# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root == None:
                return (0, True)
            left, b = height(root.left)
            right, c = height(root.right)
            if b == False or c == False:
                return (0, False)

            if abs(left-right) > 1:
                return (0, False)
            else:
                return (1 + max(left, right), True)
        return height(root)[1]
            