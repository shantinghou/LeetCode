"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        seen = {}
        def dfs(cur):
            if cur == None:
                return 
            if cur.val in seen:
                return seen[cur.val]
            seen[cur.val] = Node(cur.val)
            for n in cur.neighbors:
                if n.val in seen:
                    seen[cur.val].neighbors.append(seen[n.val])
                else:
                    seen[cur.val].neighbors.append(dfs(n))
            return seen[cur.val]
        return dfs(node)
            
            