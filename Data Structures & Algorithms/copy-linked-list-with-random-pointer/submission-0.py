"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2cpy = {None:None}

        # 1. Create all node copy
        cur = head
        while cur:
            copy = Node(cur.val)
            old2cpy[cur] = copy
            cur = cur.next

        # 2. Link all copy
        cur = head
        while cur:
            copy = old2cpy[cur]
            copy.next = old2cpy[cur.next]
            copy.random = old2cpy[cur.random]
            cur = cur.next

        return old2cpy[head]