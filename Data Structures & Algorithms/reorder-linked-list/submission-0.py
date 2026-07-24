# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. split the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        l1 = head
        l2 = slow.next
        slow.next = None # stop l1's link

        # 2. reverse list
        l2 = self.reverseList(l2)

        # 3. merge (only need to check smaller one)
        while l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next = nxt1

            l1 = nxt1
            l2 = nxt2

    def reverseList(self, head: Optional[ListNode]) -> ListNode:
        cur, prev = head, None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev