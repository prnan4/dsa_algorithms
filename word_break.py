class Solution(object):

    # ========================== APPROACH 1 ==========================
    # Recursion without memoization - Time Limit exceeded

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        def checkWordBreak(word):
            if word  == '':
                return True
            prefix_found = False
            
            n = len(word)
            
            for i in range(n +1, 0, -1):
                
                if word[0:i] in wordDict:
                    prefix_found = True
                    suffix_found = checkWordBreak(word[i:n])
        
                    if suffix_found is True: 
                        return prefix_found and suffix_found
            return False
    
    # ========================== APPROACH 2 ==========================
    # Recursion with memoization - Solution accepted. 
    # Memory is used to store the result for previously computed for words.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memory = {}
        def checkWordBreak(word):
            if word  == '':
                return True
            if word in memory:
                return memory[word]
            
            prefix_found = False
            
            n = len(word)
            
            for i in range(n +1, 0, -1):
                
                if word[0:i] in wordDict:
                    prefix_found = True
                    suffix_found = checkWordBreak(word[i:n])
        
                    if suffix_found is True:
                        memory[word] = True
                        return memory[word]
            memory[word] = False
            return memory[word]
        
        return checkWordBreak(s)