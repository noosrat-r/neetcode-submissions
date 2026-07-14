class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell - buy = profit 
        # sell >= buy, profit >= 0

        maxProfit = 0
        for i in range(len(prices)-1):
            buy = prices[i]
            for j in range(i + 1, len(prices)):
                sell = prices[j]
                profit = sell - buy
                if profit > maxProfit:
                    print(f"buy {i}: {buy}, sell {j}: {sell}, profit: {profit}")
                    maxProfit = profit

        return maxProfit