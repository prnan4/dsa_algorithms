class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        output = []
        nums.sort()
        
        def backtrack(start, combination):
            output.append(combination[:])
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                combination.append(nums[i])
                backtrack(i+1, combination)
                combination.pop()

        backtrack(0, [])
        return output
            
        