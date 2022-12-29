class Solution(object):

    # Results in time limit exceeded for large values of n
    def climbStairsRecursion(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1, 2]
        result = []
        
        def backtrack(stepsclimbed, combination):
            if stepsclimbed == n:
                result.append(combination[:])
                return
            if stepsclimbed > n:
                return
            for i in range(len(steps)):
                combination.append(steps[i])
                backtrack(stepsclimbed + steps[i], combination)
                combination.pop()
              
        backtrack(0, [])
        return len(result)

    #Using memoization
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Stores total number of ways
        memory = {1:1, 2: 2}
        
        def climb(n):
                    
            if n in memory:
                return memory[n]
            #Updating total numbe of ways to climb n stairs
            memory[n] = climb(n-1) + climb(n-2)
            return memory[n]
        return climb(n)

    def climbStairsDPBottomUP(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        
        #Stores total number of ways
        memory = [0] * (n + 1)
        
        memory[1] = 1
        memory[2] = 2
        
        for i in range(3, n+1):
            memory[i] = memory[i-1] + memory[i-2]
            
        return memory[n]
            
            