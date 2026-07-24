# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        _max = float('-inf')

        def dps(root, _max):
            if not root:
                return
            
            if root.val >= _max:
                self.res += 1
                _max = root.val

            dps(root.left, _max)
            dps(root.right, _max)

        dps(root, _max)

        return self.res

        