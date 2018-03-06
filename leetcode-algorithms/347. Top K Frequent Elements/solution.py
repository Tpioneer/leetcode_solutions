class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        topK = []
        for i in nums:
            dic[i] = dic.get(i,0)+1
        s = sorted(dic.items(), key=lambda dic:dic[1], reverse=True)
        for i in range(k):
            topK.append(s[i][0])
        return topK
        