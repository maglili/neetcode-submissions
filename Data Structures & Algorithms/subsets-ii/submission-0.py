class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        cur = []
    
        def dfs(i):
            if i==len(nums):
                res.append(cur.copy())
                return
                
            # choose num
            cur.append(nums[i])
            dfs(i+1)

            # not choose num anymoew
            cur.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)

        dfs(0)
        return res