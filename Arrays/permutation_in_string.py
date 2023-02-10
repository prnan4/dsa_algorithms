class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        a1 = [0 for _ in range(26)]
        for ch in s1:
            a1[ord(ch) - 97] += 1
        
        for i in range(0, len(s2) - len(s1) + 1):
            a2 = [0 for _ in range(26)]
            ss = s2[i: i + len(s1)]
            for ch in ss:
                a2[ord(ch) - 97] += 1
            if a1 == a2: 
                return True
        return False