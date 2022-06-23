class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        if len(s) == 1: return 1
        ch_match_list = []
        palindrome_len = 0
        for ch in s:
            if ch in ch_match_list:
                palindrome_len += 2
                ch_match_list.remove(ch)
            else:
                ch_match_list.append(ch)
        if palindrome_len < len(s):
            palindrome_len += 1
        return palindrome_len
        