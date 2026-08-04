class Solution(object):
    def maxProfit(self, prices):
        minsum=prices[0]
        profit=0
        for right in range(1,len(prices)):
            minsum=min(minsum,prices[right])
            currentprofit=prices[right]-minsum
            profit=max(profit,currentprofit)
        return profit
        