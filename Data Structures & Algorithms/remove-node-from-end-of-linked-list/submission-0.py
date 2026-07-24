# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. reverse arr
        reverse = self.reserseList(head)

        # 2. pop the node
        idx = 1
        node = reverse
        prev = None
        while node:
            nxt = node.next
            if idx == n:
                if prev == None:
                    reverse = reverse.next
                else:
                    prev.next = nxt
            prev = node
            node = nxt
            idx += 1

        # 3. reverse back
        return self.reserseList(reverse)


    def reserseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        return prev