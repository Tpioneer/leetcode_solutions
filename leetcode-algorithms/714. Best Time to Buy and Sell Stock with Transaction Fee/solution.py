# Your are given an array of integers prices,
# for which the i-th element is the price of a given stock on day i;
# and a non-negative integer fee representing a transaction fee.
# You may complete as many transactions as you like,
# but you need to pay the transaction fee for each transaction.
# You may not buy more than 1 share of a stock at a time
# (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
#
# Example 1:
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1
# Selling at prices[3] = 8
# Buying at prices[4] = 4
# Selling at prices[5] = 9
# The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.


class Solution:
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
    # time limited
    #     profits, n = [], len(prices)
    #     self.fee = fee
    #     self.dfs(prices, 0, False, 0, profits)
    #     print(profits)
    #     return max(profits)
    #
    # def dfs(self, prices, index, hold, profit, profits):
    #     fee = self.fee
    #     if index == len(prices):
    #         profits.append(profit)
    #         return
    #     else:
    #         if hold:
    #             self.dfs(prices, index + 1, False, profit + prices[index]-fee, profits)
    #             self.dfs(prices, index + 1, True, profit, profits)
    #         else:
    #             self.dfs(prices, index + 1, True, profit-prices[index], profits)
    #             self.dfs(prices, index + 1, False, profit, profits)

    # DP
        hold, empty = -prices[0], 0
        for p in prices[1:]:
            hold, empty = max(hold, empty - p), max(hold + p - fee, empty)
        return empty
