class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map_char_index = {}
        res = 0
        j = 0
        for i, ch in enumerate(s):
            if ch in map_char_index:
                j = max(j, map_char_index[ch])
                
            map_char_index[ch] = i + 1
            len_sub_string = i - j + 1
            res = max(len_sub_string, res)
        
        return res