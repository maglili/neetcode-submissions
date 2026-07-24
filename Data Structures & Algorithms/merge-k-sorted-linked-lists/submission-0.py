# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        for i, node in enumerate(lists):
            if node:
                min_heap.append(((node.val, i, node))) # i just in cast two val are the same
        heapq.heapify(min_heap)

        dummy = ListNode()
        cur = dummy
        while len(min_heap)>0:
            val, i, node = heapq.heappop(min_heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
