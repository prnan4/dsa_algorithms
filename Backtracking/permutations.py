class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        output = []
        
        def backtrack(combination):
        
            if len(combination) == len(nums):
                output.append(combination[:])
                return
            
            for i in range(0, len(nums)):
                if nums[i] in combination:
                    continue
                combination.append(nums[i])
                backtrack(combination)
                combination.pop()
        
        backtrack([])
        return output