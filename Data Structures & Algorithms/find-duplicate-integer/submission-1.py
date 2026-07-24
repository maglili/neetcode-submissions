class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd
        # 1. find the point slow meet fast
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # 2. find the loop start point
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break

        return slow2