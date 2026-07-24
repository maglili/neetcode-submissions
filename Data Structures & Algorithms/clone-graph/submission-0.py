"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        old2new = {}

        def dfs(node: Optional['Node']) -> Optional['Node']:
            if node in old2new:
                return old2new[node]

            copy_n = Node(node.val)
            old2new[node] = copy_n # update first

            for nei in node.neighbors:
                copy_n.neighbors.append(dfs(nei))

            return copy_n

        return dfs(node)