class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2

            # 如果 m 比 r 大，最小值一定在右邊
            if nums[m] > nums[r]:
                l = m + 1
            # 如果 m 比 r 小，最小值一定在左邊，可能就是 m
            else:
                r = m
        return nums[l]