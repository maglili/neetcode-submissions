class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)] # idx = freq, freq from 0 to len(num)

        for n, f in freq.items():
            bucket[f].append(n)

        res = []
        for i in range(len(nums), 0, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res