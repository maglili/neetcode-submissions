class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k  # idx in sorted array

        def quickSelect(l, r):
            p = l
            pivot = nums[r]

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[r], nums[p] = nums[p], nums[r]

            if p == k:
                return nums[p]
            elif p > k:
                return quickSelect(l, p - 1)
            else:
                return quickSelect(p + 1, r)

        return quickSelect(0, len(nums) - 1)
