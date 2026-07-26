# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node_arr = [root]

        while node_arr:
            node = node_arr.pop()

            if node.val < p.val and node.val < q.val:
                node_arr.append(node.right)
            elif node.val > p.val and node.val > q.val:
                node_arr.append(node.left)
            else:
                print(root.val)
                print(root.val)
                return root
                
                