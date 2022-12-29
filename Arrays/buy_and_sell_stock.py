class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        
        if (not prices) or (len(prices) == 1):
            return max_profit
        
        min_price = prices[0]
        
        for price in prices[1:]:
            profit = price - min_price
            
            if profit > max_profit:
                max_profit = profit 
                
            if price < min_price:
                min_price = price
                
        return max_profit