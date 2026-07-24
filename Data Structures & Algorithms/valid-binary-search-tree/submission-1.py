# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # change the bdry
        def dps(root: Optional[TreeNode], left: int, right: int) -> bool:
            if not root:
                return True

            if not (left < root.val < right):
                return False

            return dps(root.left, left, root.val) and dps(root.right, root.val, right)

        return dps(root, float('-inf'), float('inf'))