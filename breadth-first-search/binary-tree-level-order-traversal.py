# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        def traverse(root, l):
            if root == None:
                return
            if l >= len(levels):
                levels.append([])
            levels[l].append(root.val)
            traverse(root.left, l+1)
            traverse(root.right, l+1)
            return
        traverse(root, 0)
        return levels
        