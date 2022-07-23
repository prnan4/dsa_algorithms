class Solution(object):
    #========================== APPROACH 1 ==========================
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

    #========================== APPROACH 2 ==========================
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
    
    # ========================== APPROACH 3 ==========================  
    #Recursion with memoization using 1D array
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

    #========================== APPROACH 4 ==========================  
    # Dynamic Programming bottom up using 1D array
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
        
    #========================== APPROACH 5 ==========================
    # Unbounded knapsack style, recursive without memoization

    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def minCoins(amount, coins):
            
            if amount == 0:
                return 0
            if len(coins)==0:
                return float('inf') - 1
            
            if (coins[len(coins)- 1] <= amount):
                return min(minCoins(amount - coins[len(coins)- 1], coins) +  1, minCoins(amount , coins[:-1]))
            else:
                return minCoins(amount , coins[:-1])
        
        result = minCoins(amount, coins)
        if result == float('inf'):
            return -1
        return result


    #========================== APPROACH 5 ==========================
    # Unbounded knapsack style, recursive with memoization
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        memory = [[float('inf') for _ in range(len(coins) + 1)] for _ in range(amount +1)]
        def minCoins(amount, coins):
        
            if amount == 0:
                return 0
            if len(coins)==0:
                return float('inf') - 1

            if memory[amount][len(coins)] != float('inf'): 
                return memory[amount][len(coins)]
            
            if (coins[len(coins)- 1] <= amount):
                memory[amount][len(coins)] = min(minCoins(amount - coins[len(coins)- 1], coins) +  1, minCoins(amount , coins[:-1])) 
            else:
                memory[amount][len(coins)] =  minCoins(amount , coins[:-1])
            return memory[amount][len(coins)]
        
        result = minCoins(amount, coins)
        if result == float('inf'):
            return -1
        return result