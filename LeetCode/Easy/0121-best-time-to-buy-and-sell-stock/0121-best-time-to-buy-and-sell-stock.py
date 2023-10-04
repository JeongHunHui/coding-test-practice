class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = prices[0], 0

        for i in range(1, len(prices)):
            current_price = prices[i]
            max_profit = max(current_price-min_price, max_profit)
            min_price = min(current_price, min_price)

        return max_profit