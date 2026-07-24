# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque([root])

        while queue:
            sub_list = []
            fifo_len = len(queue) # key: num of node in layer

            for i in range(fifo_len):
                node = queue.popleft()
                if node:
                    sub_list.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                    
            if sub_list:
                res.append(sub_list)

        return res

