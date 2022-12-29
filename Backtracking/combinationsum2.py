class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        output = []
        combination = []
        candidates.sort()
        
        def backtrack(subtotal, combination, start):
            
            if subtotal == target: 
                output.append(combination[:])
                return
            if subtotal > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                combination.append(candidates[i])
                backtrack(subtotal + candidates[i], combination, i +1)
                combination.pop()
                
        backtrack(0, [], 0)
                
        return output