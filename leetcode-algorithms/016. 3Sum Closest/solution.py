# Given an array nums of n integers and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
#
# Example:
#
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    return sum
                if abs(sum - target) < abs(result - target):
                    result = sum
                if sum < target:
                    j += 1
                elif sum > target:
                    k -= 1
        return result

    # time limited
    #     if len(nums) < 3:
    #         return
    #     res = []
    #     self.dfs(nums, 3, target, 0, [], res)
    #     min_t = abs(res[0]-target)
    #     ans = res[0]
    #     print(res)
    #     for i in res:
    #         if abs(i-target) < min_t:
    #             min_t = abs(i-target)
    #             ans = i
    #     return ans
    #
    # def dfs(self, nums, k, target, index, path, res):
    #     if k == 0:
    #         res.append(sum(path))
    #     for i in range(index, len(nums)):
    #         self.dfs(nums, k - 1, target, i + 1, path + [nums[i]], res)

