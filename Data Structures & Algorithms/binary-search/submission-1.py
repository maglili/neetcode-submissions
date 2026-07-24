class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while (l < r):
            idx = int((l + r) / 2)
            print(idx)
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                r = idx
            else:
                l = idx + 1
        return -1
