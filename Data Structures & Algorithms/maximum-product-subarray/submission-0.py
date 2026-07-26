class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        G = [0] * n # max product end with ith num
        H = [0] * n # min product end with ith num
        G[0] = H[0] = nums[0]

        for i in range(1, n):
            G[i] = max(nums[i], nums[i]*G[i-1], nums[i]*H[i-1])
            H[i] = min(nums[i], nums[i]*G[i-1], nums[i]*H[i-1])

        return G[n-1]