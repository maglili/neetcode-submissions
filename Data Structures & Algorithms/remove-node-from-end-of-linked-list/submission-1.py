# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dmy = ListNode()
        dmy.next = head
        
        # [1,2,3,4]
        # dmy, 1, 2, 3, 4, N
        #
        l, r = dmy, head

        # init r
        cnt = 0
        while r and cnt < n:
            r = r.next
            cnt += 1
        
        # go through the end to get right l
        while r:
            l = l.next
            r = r.next
        
        # update l.next
        l.next = l.next.next

        return dmy.next
             