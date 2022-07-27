class Solution(object):
    # ========================== APPROACH 1 ==========================
    # Top down Recursion without memoization
    def longestCommonSubsequence(self, t1, t2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # Base condition: If either of t1 or t2 is empty string
        if (not t1) or (not t2):
            return 0
        
        match_index = -1
        for i in range(len(t2)):
            if t1[0] == t2[i]:
                match_index = i
                break
        if match_index == -1:
            include = 0
        else:
            include = 1 + self.longestCommonSubsequence(t1[1:], t2[match_index + 1:])
        dont_include = self.longestCommonSubsequence(t1[1:], t2)
        return max(include, dont_include)

    # ========================== APPROACH 2 ==========================
    # Top down Recursion with memoization
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        memory = [[None for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        for i in range(len(text2) + 1):
            memory[0][i] = 0
        for j in range(len(text1) + 1):
            memory[j][0] = 0  
            
        def maxLengthCommonSubsequence(t1, t2):
            # Base condition: If either of t1 or t2 is empty string
            l_t1 = len(t1)
            l_t2 = len(t2)
            if memory[l_t1][l_t2] is not None:
                return memory[l_t1][l_t2] 

            match_index = -1
            for i in range(len(t2)):
                if t1[0] == t2[i]:
                    match_index = i
                    break
            if match_index == -1:
                include = 0
            else:
                include = 1 + maxLengthCommonSubsequence(t1[1:], t2[match_index + 1:])
            dont_include = maxLengthCommonSubsequence(t1[1:], t2)
            memory[l_t1][l_t2] = max(include, dont_include)
            return memory[l_t1][l_t2] 
        
        return maxLengthCommonSubsequence(text1, text2)


    # ========================== APPROACH 3 ==========================
    # Bottom up DP
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        l1 = len(text1)
        l2 = len(text2)
        
        memory = [[None for _ in range(l2 + 1)] for _ in range(l1 + 1)]
        for i in range(l2 + 1):
            memory[0][i] = 0
        for j in range(l1 + 1):
            memory[j][0] = 0  
            
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if text1[i-1] == text2[j-1]:
                    memory[i][j] = 1 + memory[i-1][j-1]
                else:
                    memory[i][j] = max(memory[i-1][j], memory[i][j-1])
            
        return memory[l1][l2]




