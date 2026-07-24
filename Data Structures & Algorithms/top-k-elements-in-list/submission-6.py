class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)

        minheap = []
        
        for n, f in freq.items():
            heapq.heappush(minheap, (f, n))

            if len(minheap) > k:
                heapq.heappop(minheap)
        
        return [n for (f, n) in minheap]