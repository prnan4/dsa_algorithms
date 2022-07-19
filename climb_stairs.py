class Solution(object):
    #USing memoization
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memory = {1:1, 2:2}
        
        def climb(n):
            if n not in memory:
                memory[n] = climb(n-1) + climb(n-2)
            return memory[n]
        return climb(n)


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