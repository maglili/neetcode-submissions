class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs():
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                
                if nums[i] in cur:
                    continue

                cur.append(nums[i])
                dfs()

                cur.pop()

        dfs()
        return res