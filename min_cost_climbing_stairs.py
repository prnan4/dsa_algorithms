class Solution(object):
    def minCostClimbingStairs(self, cost):
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