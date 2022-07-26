class Solution(object):
    # Recursion without memoization
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        def maxWays(m, n):
            # Exit condition
            if m == 0 and n == 0:
                return 1
            
            # Edge case
            elif n == 0: 
                return maxWays(m-1, n)
            elif m == 0:
                return maxWays(m, n-1)
            else:
                return (maxWays(m, n-1) + maxWays(m-1, n))
        
        return maxWays(m-1, n-1)

    # Recursion with memoization
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memory = [[None for _ in range(n)] for _ in range(m)]
        memory[0][0] = 1
        
        def maxWays(m, n):
            # If value is calculated and can be found in memory
            if memory[m][n]: 
                return memory[m][n]
 
            elif n == 0: 
                memory[m][n] = maxWays(m-1, n)
            elif m == 0:
                memory[m][n] = maxWays(m, n-1)
            else:
                memory[m][n] = maxWays(m, n-1) + maxWays(m-1, n)
            return memory[m][n] 
        
    # Bottom up DP
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memory = [[None for _ in range(n)] for _ in range(m)]
        memory[0][0] = 1
        
        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    memory[i][j] = memory[i][j-1]
                elif j == 0:
                    memory[i][j] = memory[i-1][j]
                else:
                    memory[i][j] = memory[i][j-1] + memory[i-1][j]
        return memory[m-1][n-1]          

    # Bottom up DP optimized
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        memory = [[None for _ in range(n)] for _ in range(m)]
         
        for i in range(0, m):
            for j in range(0, n):
                if j == 0 or i == 0:
                    memory[i][j] = 1 
                else:
                    memory[i][j] = memory[i][j-1] + memory[i-1][j]
                
        return memory[m-1][n-1]  
                
        
        
        
        
        