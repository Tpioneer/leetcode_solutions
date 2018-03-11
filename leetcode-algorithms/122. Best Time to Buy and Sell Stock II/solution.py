class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0 or len(prices)==1:
            return 0
        max_pro = 0
        for i in range(len(prices)-1,0,-1):
            if prices[i]-prices[i-1] > 0:
               max_pro += prices[i]-prices[i-1]
        return max_pro