class MedianFinder:

    def __init__(self):
        self.max_heap = [] # first half
        self.min_heap = [] # second half

    def addNum(self, num: int) -> None:

        # add num to left always
        heapq.heappush(self.max_heap, -num)
        # then pop the max num to right to balance the num
        val = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, val)

        # if right bigger than left, push node back to left
        if len(self.min_heap) > len(self.max_heap):
            pop_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -pop_num)

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) % 2 == 0:
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]
        