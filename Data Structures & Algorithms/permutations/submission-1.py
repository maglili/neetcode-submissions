class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []

        def dfs():
            # base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                # skip the num already choose
                if nums[i] in cur:
                    continue

                # choose case
                cur.append(nums[i])
                dfs()

                # not choose case
                cur.pop()

        dfs()
        return res