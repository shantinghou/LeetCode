# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def greatest(root, largest):
            if root == None:
                return 0
            num = 0
            if root.val >= largest:
                largest = root.val
                num += 1
            numL = greatest(root.left, largest)
            numR = greatest(root.right, largest)
            return numL + numR + num
        return greatest(root, -10000)