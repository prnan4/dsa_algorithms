class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        out = []
        res = []
        def isPalindrome(s):
            return True if s[::-1] == s else False

        def partitionInput(s, c):
            if s == '':
                out.append(c[:])
                return
            for i in range(0, len(s)):
                ss = s[0:i+1]
                rem = s[i+1:len(s)]
                if isPalindrome(ss):
                    res.append(ss)
                    partitionInput(rem, res)
                    res.pop()
                
        partitionInput(s, [])

        return out