class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        appear = {}
        for i in nums:
            if i in appear:
                return i
            else:
                appear[i] = True
