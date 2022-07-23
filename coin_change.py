class Solution(object):
    # Pure recursion. Time limit exceeded
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort(reverse=True)
        output = []
        
        def backtrack(total, combination, start):
            if total == amount: 
                output.append(combination[:])
                return
            if total > amount: return
            for i in range(start, len(coins)):
                combination.append(coins[i])
                backtrack(total + coins[i], combination, i)
                combination.pop()


        backtrack(0, [], 0)
        if not output: return -1
        result = len(output[0])
        for combination in output[1:]:
            result = min(result, len(combination))
        return result

    # Without memoization
    def coinChangeRecursionStoringRemainingAmount(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        def getMinCoins(coins, amount):
            if amount == 0:
                return 0
            
            result = float('inf')    
            if amount <0:
                return result
               
            for i in range(len(coins)):
                ways = 1 + getMinCoins(coins, amount - coins[i])
                result = min(result, ways)
            return result
        
        result = getMinCoins(coins, amount)
        if result == float('inf'): return -1
        else: return result
        
    #Recursion with memoization
    def coinChangeRecursionWithMemoization(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        memory = {}
        def getMinCoins(amount):
            
            if amount in memory: return memory[amount]
            
            if amount == 0:
                return 0
                
            if amount <0:
                return float('inf')
            
            result = float('inf')
            for i in range(len(coins)):
                ways = 1 + getMinCoins(amount - coins[i])
                result = min(result, ways)
            
            memory[amount] = result
            return result
        
        result = getMinCoins(amount)
        if result == float('inf'): return -1
        else: return result
        
    # Dynamic Programming bottom up
    def coinChangeDP(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        amounts = [float('inf')] * (amount + 1)
        amounts[0] = 0
        
        for i in range(len(amounts)):
            for j in range(len(coins)):
                if coins[j] <= i:
                    amounts[i] = min(amounts[i], 1 + amounts[i - coins[j]])
        
        if amounts[amount] == float('inf'): return -1 
        return amounts[amount]
        