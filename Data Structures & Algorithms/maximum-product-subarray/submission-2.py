class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        max_p = 1 # max product
        min_p = 1 # min product
        res = nums[0]

        for i in nums:
            temp = max_p * i
            
            max_p = max(i, temp, min_p * i)
            min_p = min(i, temp,  min_p * i)

            if max_p > res:
                res = max_p

        return res