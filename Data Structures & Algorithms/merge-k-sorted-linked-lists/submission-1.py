# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            new_list = []
            for i in range(0, len(lists), 2):
                head1 = lists[i]
                head2 = lists[i+1] if i+1 < len(lists) else None
                new_list.append(self.merge(head1, head2))
            lists =     new_list
        return lists[0]

    def merge(self, head1 :ListNode, head2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while head1 and head2:
            if head1.val <= head2.val:
                cur.next = head1
                head1 = head1.next
            else:
                cur.next = head2
                head2 = head2.next
            cur = cur.next

        if head1:
            cur.next = head1
        else:
            cur.next = head2

        return dummy.next
