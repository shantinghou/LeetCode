# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def seek(root, subRoot):
            if subRoot == None and root == None:
                return True
            if (root == None and subRoot != None) or (root != None and subRoot == None):
                return False
            if root.val != subRoot.val:
                return False
            return seek(root.left, subRoot.left) and seek(root.right, subRoot.right)

        def explore(root):
            tried = False
            if root == None:
                return False
            if root.val == subRoot.val:
                tried = seek(root, subRoot)
            return tried or explore(root.left) or explore(root.right)
        return explore(root) 