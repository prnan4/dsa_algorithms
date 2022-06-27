class Solution(object):
    
    def checkSubstringForMoreThanTwoDistinct(self, ch_count):
        return False if len(ch_count)<=2 else True
        
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_count = {}
        i = 0
        res = 0
        for j, ch in enumerate(s):
            if ch in ch_count: ch_count[ch] += 1
            else: ch_count[ch] = 1
            while self.checkSubstringForMoreThanTwoDistinct(ch_count):
                i += 1
                ch_count[s[i-1]] -= 1
                if ch_count[s[i-1]] == 0: del ch_count[s[i-1]]
            res = max(res, j-i+1)
        return res

    # Optimisation
    def lengthOfLongestSubstringTwoDistinctOptimised(self, s):
        """
        :type s: str
        :rtype: int
        """
        ch_count = {}
        i = 0
        res = 0
        for j, ch in enumerate(s):
            ch_count[ch] = j
            if self.checkSubstringForMoreThanTwoDistinct(ch_count):
                i = min(ch_count.values()) + 1
                del ch_count[s[i-1]]
            res = max(res, j-i+1)
        return res
            
            