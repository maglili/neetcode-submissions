# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.chk_match(root, subRoot) == True:
            return True

        return self.chk_match(root.left, subRoot) or self.chk_match(root.right, subRoot)

    def chk_match(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif p and q and p.val == q.val:
            return self.chk_match(p.left, q.left) and self.chk_match(p.right, q.right)
        else:
            return False
