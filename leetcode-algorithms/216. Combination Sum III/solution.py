# Find all possible combinations of k numbers that add up to a number n,
# given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]


class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        # 纯迭代求出所有k的排列
        # combs = [[i] for i in range(1,10)]
        # for _ in range(k-1):
        #     combs = [[first] + comb
        #              for comb in combs
        #              for first in range(1, comb[0])]
        #     print(combs)
        # return [c for c in combs if sum(c) ==n]

        # backtracking(dfs)
        res = []
        self.dfs(range(1, 10), k, n, 0, [], res)
        return res

    def dfs(self, nums, k, n, index, path, res):
        if k < 0 or n < 0:  # backtracking
            return
        if k == 0 and n == 0:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, k - 1, n - nums[i], i + 1, path + [nums[i]], res)

