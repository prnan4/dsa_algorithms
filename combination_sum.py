class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        output = []
        
        def findCombinations(i, subtotal, combination):
            
            if subtotal == target:
                output.append(combination[:])
                return
            if subtotal > target or i == len(candidates):
                return
            
            combination.append(candidates[i])
            findCombinations(i, subtotal + candidates[i], combination)
            combination.pop()
            findCombinations(i+1, subtotal, combination)
        
        findCombinations(0, 0, [])
        return output