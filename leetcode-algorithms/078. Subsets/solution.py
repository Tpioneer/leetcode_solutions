# Given a set of distinct integers, nums, return all possible subsets (the power set).
# Note: The solution set must not contain duplicate subsets.
#
# Example:
# Input: nums = [1,2,3]
# Output:
#  [[3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []]


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
    #     res = [[]]
    #     for k in range(0, len(nums)):
    #         temp = []
    #         self.dfs(nums, 0, k+1, [], temp)
    #         res += temp
    #     return res
    #
    # def dfs(self, nums, index, k, path, res):
    #     if k == 0:
    #         res.append(path)
    #         return
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, i + 1, k-1, path + [nums[i]], res)

    #     res = []
    #     self.dfs(sorted(nums), 0, [], res)
    #     return res
    #
    # def dfs(self, nums, index, path, res):
    #     res.append(path)
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, i + 1, path + [nums[i]], res)
        res = [[]]
        for num in sorted(nums):
            res += [item + [num] for item in res]
        return res

