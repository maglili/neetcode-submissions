class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}  # key: ()

        def dfs(i, _sum):
            if i == len(nums):
                return 1 if _sum == target else 0
            
            if (i, _sum) in memo:
                return memo[(i, _sum)]

            res = 0
            res += dfs(i + 1, _sum + nums[i])
            res += dfs(i + 1, _sum - nums[i])

            memo[(i, _sum)] = res
            return res

        return dfs(0, 0)
