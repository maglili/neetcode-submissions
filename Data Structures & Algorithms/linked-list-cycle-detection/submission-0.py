# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
    
        s1 = head
        if head.next:
            s2 = head.next.next
        else:
            s2 = None
        while s1 and s2:
            if s1.val == s2.val:
                return True
            if s1.next:
                s1 = s1.next
            if s2.next:
                s2 = s2.next.next
        return False
         
            


