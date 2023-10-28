class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        l = 0
        r = 0
        max_len = 0
        char_dict = {}
        while r < len(s):
            if s[r] in char_dict:
                l = max(l, char_dict[s[r]] + 1)
            char_dict[s[r]] = r
            r += 1
            max_len = max(max_len, r-l)
        return max_len
        