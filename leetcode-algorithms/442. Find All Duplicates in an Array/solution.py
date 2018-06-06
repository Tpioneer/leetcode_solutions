# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array),
# some elements appear twice and others appear once.
# Find all the elements that appear twice in this array.
# Could you do it without extra space and in O(n) runtime?


class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            index = abs(nums[i])-1
            if nums[index] < 0:
                res.append(index+1)
            else:
                nums[index] = -nums[index]
        return res
