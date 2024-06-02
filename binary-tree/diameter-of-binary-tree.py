# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        dia = left + right
        return max(dia, max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right)))