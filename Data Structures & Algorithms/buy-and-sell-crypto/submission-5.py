class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sell - buy = profit 
        # sell >= buy, profit >= 0

        # maxProfit = 0
        # for i in range(len(prices)-1):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell = prices[j]
        #         profit = sell - buy
        #         if profit > maxProfit:
        #             print(f"buy {i}: {buy}, sell {j}: {sell}, profit: {profit}")
        #             maxProfit = profit

        # return maxProfit

        # can probably optimize the inner loop
        # order needs to stay the same
        # maybe we could use an extra data structure?
        buy = 0
        sell = buy + 1
        maxProfit = 0
        while sell < len(prices):
            if prices[sell] <= prices[buy]:
                buy = sell
            elif prices[sell] > prices[buy]:
                maxProfit = max(maxProfit, prices[sell]-prices[buy])
            sell += 1
        
        return maxProfit