class Solution(object):

    # ========================== APPROACH 1 ==========================
    # Recursion without memoization 

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
    """
    ['penapple'] ['pen', 'apple']
    
    ['penapple'] [ 'pe', 'pen', 'apple']
    """

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

    # ========================== APPROACH 3 ==========================
    # Bottom up DP
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memory = [False for _ in range(len(s)+1)]
        memory[0] = True
        
        for i in range(1, len(s)+1):
            for j in range(0, i):
                if memory[j] and (s[j:i] in wordDict):
                    memory[i] = True
                    break
        return memory[len(s)]