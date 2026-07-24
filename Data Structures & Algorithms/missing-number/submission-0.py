class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        gold = 0
        for i in range(len(nums)+1):
            gold += i
        print(gold)

        res = 0
        for n in nums:
            res += n
        return gold - res