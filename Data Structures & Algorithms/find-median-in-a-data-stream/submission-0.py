class MedianFinder:

    def __init__(self):
        self.h_small = [] # max_heap, 1st half of array, smaller one
        self.h_large = [] # min_heap, 2nd half of array, large one
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        heapq.heappush(self.h_small, num)

        if abs(len(self.h_small) - len(self.h_large)) > 1:
            large = self.h_small if len(self.h_small) > len(self.h_large) else  self.h_large
            small = self.h_small if large == self.h_large else self.h_large
            pop_node =  heapq.heappop(large)
            heapq.heappush(small, pop_node)

    def findMedian(self) -> float:
        if (self.count % 2) == 0:
            return (self.h_small[0] + self.h_large[0]) / 2
        return self.h_small[0]