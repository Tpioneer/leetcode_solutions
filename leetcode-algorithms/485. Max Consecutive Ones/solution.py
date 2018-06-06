# Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_number = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                max_number = max(count, max_number)
                count = 0
        return max(max_number, count)
