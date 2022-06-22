class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        match_dict = {'}':'{',')':'(', ']':'['}
        
        for ch in s:
            if ch in ['(', '{', '[']:
                stack.append(ch)
            
            elif ch in [')', '}', ']']:
                if not stack: return False
                ele = stack.pop()
                if ele != match_dict[ch]: return False
                
        return True if not stack else False
                    