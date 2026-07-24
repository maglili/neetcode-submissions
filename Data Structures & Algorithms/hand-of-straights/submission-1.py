from collections import deque
import heapq


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        cnt_tbl = Counter(hand)
        minheap = [k for k in cnt_tbl.keys()]
        heapq.heapify(minheap)

        while minheap:
            start = minheap[0]
            for i in range(start, start + groupSize):
                if i not in cnt_tbl:
                    return False
                cnt_tbl[i] -= 1
                if cnt_tbl[i] == 0:
                    if i != minheap[0]:
                        return False
                    heapq.heappop(minheap)
        return True
