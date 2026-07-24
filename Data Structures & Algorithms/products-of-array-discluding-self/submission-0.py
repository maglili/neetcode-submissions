class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        ans = [ 1 for _ in nums]

        for i in range(len(nums)):
            num = nums[i]
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    ans[j] *= num

        return ans

        

        