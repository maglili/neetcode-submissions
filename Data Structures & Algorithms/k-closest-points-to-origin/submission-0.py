import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            x,y = points[i]
            dis = math.sqrt(x**2+y**2)
            heapq.heappush(pq, (dis, i)) # (dis, idx)
        
        res = []
        for i in range(k):
            (dis, i) = heapq.heappop(pq)
            res.append(points[i])
        return res