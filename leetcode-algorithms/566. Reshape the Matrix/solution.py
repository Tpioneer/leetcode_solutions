class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        if len(nums) > 0:
            a = len(nums)
            b = len(nums[0])
            if r * c != a * b:
                return nums
            else:
                m = []
                for i in range(a):
                    for j in range(b):
                        m.append(nums[i][j])
                row = []
                co = []
                for i in range(r):
                    for j in range(c):
                        row.append(m[i*c+j])
                    co.append(row)
                    row = []
                return co