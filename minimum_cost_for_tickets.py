class Solution(object):
    # ========================== APPROACH 1 ==========================  
    #Recursion without memoization
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        len_days = [1, 7, 30]
        
        def getMinCost(days):
        
            if not days: 
                return 0
            
            result = float('inf')
            for i in range(len(costs)):
                
                days_end = days[0] + len_days[i]
                days_copy = [j for j in days if j >= days_end]
                cost = costs[i] + getMinCost(days_copy)
                result = min(result, cost)
            
            return result
        return getMinCost(days)


    # ========================== APPROACH 2 ==========================  
    #Recursion with memoization. Memorising the length of days array.
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        
        len_days = [1, 7, 30]
        memory = {}
        
        def getMinCost(days):
        
            if len(days) in memory:
                return memory[len(days)]
            
            if not days: 
                return 0
            
            result = float('inf')
            for i in range(len(costs)-1, -1, -1):
                
                days_end = days[0] + len_days[i]
                days_copy = [j for j in days if j >= days_end]
                cost = costs[i] + getMinCost(days_copy)
                result = min(result, cost)
            
            memory[len(days)] = result
            return result
        return getMinCost(days)