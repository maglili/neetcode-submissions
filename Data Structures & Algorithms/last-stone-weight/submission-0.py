import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)

        while len(q) > 1:
            stone1 = heapq.heappop(q)
            stone2 = heapq.heappop(q)
            heapq.heappush(q, stone1 - stone2)
        
        return -1 * q[0]
