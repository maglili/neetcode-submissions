class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(i, cur_sum):
            if cur_sum == target:
                res.append(cur.copy())
                return

            if i >= len(nums) or cur_sum > target:
                return
            
            # choose same num
            cur.append(nums[i])
            dfs(i, cur_sum + nums[i])

            # not choose the num anymore
            cur.pop()
            dfs(i+1, cur_sum)
        
        dfs(0, 0)
        return res