class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        _min = nums[l]

        while l <= r:
            m = (l + r) // 2
            _min = min(_min, nums[m])

            if nums[l] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return _min
            