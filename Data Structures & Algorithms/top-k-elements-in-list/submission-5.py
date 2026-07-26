class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        minheap = []
        
        for k, v in freq.items():
            heapq.heappush(minheap, (v, k))

            if len(minheap) > 2:
                heapq.heappop(minheap)
        
        return [k for (v, k) in minheap]