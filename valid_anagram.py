class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        
        char_dict = {}
        for i in range(97, 123):
            char_dict[chr(i)] = 0
            
        for j in range(len(s)):
            char_dict[s[j]] += 1
            char_dict[t[j]] -= 1
        
        # any(char_dict.values()) is False if all elements of list are 0
        return not any(char_dict.values())
        