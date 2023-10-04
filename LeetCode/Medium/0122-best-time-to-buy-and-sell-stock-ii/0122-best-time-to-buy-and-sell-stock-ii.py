class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_price, current_profit = prices[0], 0
        total_profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            print(pre_price, current_price, current_profit, total_profit)
            if pre_price > current_price:
                total_profit += current_profit
                pre_price = current_price
                current_profit = 0
            else:
                current_profit += current_price - pre_price
                pre_price = current_price
            
        return total_profit + current_profit