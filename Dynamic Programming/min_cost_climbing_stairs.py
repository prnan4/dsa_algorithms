class Solution(object):

    # ========================== APPROACH 1 ==========================
    def minCostClimbingStairsRecursionWithMemoization(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #Stores minimum cost
        memory = {}
        
        def minCostToClimb(n):
                   
            # Base condition
            if n <= 1: 
                return 0
            
            if n in memory: 
                return memory[n]
            
            # Cost required to reach final step by climbing one step previously is equal to cost paid at previous step plus minimum cost to reach up until that step
            cost_by_one = cost[n-1] + minCostToClimb(n-1)
            # Cost required to reach final step by climbing two steps  previously is equal to cost paid at second last step plus minimum cost to reach up until that step
            cost_by_two = cost[n-2] + minCostToClimb(n-2)
            
            # Updating minimum cost to climb n stairs
            memory[n] = min(cost_by_one, cost_by_two)
            
            return memory[n]
            
        return minCostToClimb(len(cost))

    # ========================== APPROACH 2 ==========================
    def minCostClimbingStairsDPBottomUp(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        #Stores minimum cost
        memory = [float('inf')] * (len(cost) + 1)
        
        memory[0] = 0
        memory[1] = 0
        
        for i in range(2, len(cost)+1):
            memory[i] = min(cost[i-1] + memory[i-1], cost[i-2] + memory[i-2])
        return memory[len(cost)]