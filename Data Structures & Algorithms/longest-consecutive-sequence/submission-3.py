class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. put all num in tbl
        num_set = set(nums)

        # 2. scan all nums
        res = 0
        for n in nums:
            # impossible to be the start of the sequence
            if n - 1 in num_set:
                continue

            length = 1
            while (n + length) in num_set:
                length += 1
            res = max(res, length)
        return res
