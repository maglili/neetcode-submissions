class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_tbl = {}
        for i in range(len(nums)):
            rest_num = target - nums[i]
            if rest_num in seen_tbl:
                return [seen_tbl[rest_num], i]
            else:
                seen_tbl[nums[i]] = i