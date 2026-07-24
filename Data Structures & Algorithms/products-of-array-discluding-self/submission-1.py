class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_pructs = [ 1 for _ in nums ]
        product = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            product = nums[i-1] * product
            pre_pructs[i] = product

        suf_pructs = [ 1 for _ in nums ]
        product = 1
        for i in reversed(range(len(nums))):
            if i == (len(nums) - 1):
                continue
            product = nums[i+1] * product
            suf_pructs[i] = product

        return [pre_pructs[i] * suf_pructs[i] for i in range(len(nums))]

