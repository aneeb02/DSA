'''
You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
'''


from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 1
        profit = 0
        while sell < len(prices):
            if prices[buy] < prices[sell]:
                p = prices[sell] - prices[buy]
                profit = max(profit, p)
            else: 
                buy = sell
            
            sell += 1
        return profit