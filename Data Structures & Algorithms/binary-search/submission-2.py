class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1  
        while (l <= r):
            idx = int((l + r) / 2)
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = idx - 1
            else:
                l = idx + 1
        return -1
