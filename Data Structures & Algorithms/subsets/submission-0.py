class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i: int):
            if i >= len(nums):
                res.append(cur.copy())
                return
            
            # choose i-th num path
            cur.append(nums[i])
            dfs(i+1)

            # not choose i-th num
            cur.pop()
            dfs(i+1)

        dfs(0)
        return res