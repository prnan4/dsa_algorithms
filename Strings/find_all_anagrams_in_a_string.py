class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(p) > len(s):
            return []
        p_dict = {}
        for ch in p:
            if ch in p_dict:
                p_dict[ch] += 1
            else:
                p_dict[ch] = 1
            
        s_dict = {}
        for i in range(0, len(p)):
            ch = s[i]
            if ch in s_dict:
                s_dict[ch] += 1
            else:
                s_dict[ch] = 1
        
        res = []
        for i in range(0, len(s) - len(p) + 1):
            if i != 0:    
                ch = s[i + len(p) -1]
                if ch in s_dict:
                    s_dict[ch] += 1
                else:
                    s_dict[ch] = 1
            if s_dict == p_dict:
                res.append(i)
            s_dict[s[i]] -= 1
            if(s_dict[s[i]] == 0):
                del s_dict[s[i]]
        return res