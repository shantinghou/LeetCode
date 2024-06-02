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
        dia = [0]
        def dfs(root):
            if root == None:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            total = left + right + 2
            dia[0] = max(dia[0], total)
            return max(left, right) + 1
        dfs(root)
        return dia[0]