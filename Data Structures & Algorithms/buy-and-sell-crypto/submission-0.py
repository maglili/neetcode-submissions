class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_prof = 0
        for num in prices:
            max_prof = max(max_prof, num - min_price)
            min_price = min(min_price, num)
        return max_prof