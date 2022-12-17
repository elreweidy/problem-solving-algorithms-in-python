class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        today, future = 0, 1
        maxprofit = 0

        while future < len(prices):
            if prices[today] < prices[future]:
                profit = prices[future] - prices[today]
                maxprofit = max(maxprofit, profit)
            else:
                today = future
            future += 1

        return maxprofit