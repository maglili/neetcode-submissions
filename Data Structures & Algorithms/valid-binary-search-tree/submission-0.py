# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root) -> bool:
            if not root:
                return True

            if root.left and  root.left.val >= root.val:
                return False
            if root.right and  root.right.val <= root.val:
                return False

            return dfs(root.left) and  dfs(root.right)

        return dfs(root)
            
        