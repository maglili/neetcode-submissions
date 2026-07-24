import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # counter freq of each char
        freq = Counter(tasks)
        
        # build max-heap
        heap = []
        for k,v in freq.items():
            heap.append(v * -1) # mul -1 for max heap
        heapq.heapify(heap)

        # init fifo
        fifo = deque([]) # (job_freq, cycle)
        cycle = 0
        while len(heap) > 0 or len(fifo) > 0:
            cycle += 1
            # choose max freq job from heap, and push it into queue
            if len(heap) > 0:
                f = heapq.heappop(heap)
                f += 1
                if f != 0:
                    fifo.append((f, cycle+n))
            
            if len(fifo) > 0:
                if cycle >= fifo[0][1]:
                    j,c = fifo.popleft()
                    heapq.heappush(heap, j)


        return cycle