class Solution(object):
    def minFlipsMonoIncr(self, s):
        """
        :type s: str
        :rtype: int
        """

        flips = 0
        ones = 0

        for c in s:
            if c == '0':
                flips += 1
            else:
                ones += 1
            flips = min(flips, ones)
        return flips
            