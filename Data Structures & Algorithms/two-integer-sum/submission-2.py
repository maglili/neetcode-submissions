class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tbl = {} # {num: idx}
        for idx, n in enumerate(nums):
            if (target - n) in tbl:
                return [tbl[(target - n)], idx]
            tbl[n] = idx