# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        seenLeft = self.rightSideView(root.left)
        seenRight = self.rightSideView(root.right)
        total = [root.val] + seenRight
        if len(seenLeft) > len(seenRight):
            total += seenLeft[len(seenRight):]
        return total