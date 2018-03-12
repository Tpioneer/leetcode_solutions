class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = {}
        count = 0
        AB = [a+b for a in A for b in B]
        for i in AB:
            dic[i] = dic.get(i,0) + 1
        CD = [-(c+d) for c in C for d in D]
        for i in CD :
            if i in dic.keys():
                count += dic[i]
        return count
                