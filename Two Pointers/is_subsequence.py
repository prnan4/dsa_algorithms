class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0

        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                j += 1
            i += 1

        return True if j == len(s) else False
