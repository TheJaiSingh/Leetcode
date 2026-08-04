class Solution(object):
    def maxProfit(self, prices):
        profit=0
        for right in range(1,len(prices)):
            if prices[right]>prices[right-1]:
                profit+=prices[right]-prices[right-1]
        return profit
        
        