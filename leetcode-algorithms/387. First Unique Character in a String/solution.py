class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for x in s:
            dic[x] = dic.get(x, 0) + 1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1