import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pq = []
        for i in range(len(points)):
            x,y = points[i]
            dis = x**2+y**2
            heapq.heappush(pq, (-1*dis, i)) # (dis, idx)

            if len(pq) > k:
                heapq.heappop(pq)
        
        res = []
        for i in range(k):
            (dis, i) = heapq.heappop(pq)
            res.append(points[i])
        return res