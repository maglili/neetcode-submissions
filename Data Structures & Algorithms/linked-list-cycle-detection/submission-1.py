# Definition for singly-linked list.
# class ListNode: 
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False

        s1 = head
        if head.next:
            s2 = head.next
        else:
            s2 = None

        while s1 and s2:
            if s1 == s2:
                return True
            s1 = s1.next
            if s2.next:
                s2 = s2.next.next
            else:
                s2 = None
        return False