class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        def appendToOutput(num):
            if not output:

                output.append([])
                output.append([num])
            else:
                temp = output[:]
                for ele in temp:
                    if not ele:
                        print("k")
                        output.append([num])
                    else:
                        temp2 = ele[:]
                        temp2.append(num)
                        output.append(temp2)


        for num in nums:
            appendToOutput(num)
        
        return output

    def subsetsRecursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        subset = []
        def backtrack(i):
            
            if i == len(nums):
                output.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i+1)
            
            subset.pop()
            backtrack(i+1)
            
        backtrack(0)
        return output

    def subsetsMethod2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        
        def backtrack(start, combination):
            output.append(combination[:])
            for i in range(start, len(nums)):
                combination.append(nums[i])
                backtrack(i+1, combination)
                combination.pop()
        backtrack(0, [])
        return output
    
    # October 15 2023
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        combination = []
        result = []
        it = 0

        def backtrack(it, combination):
            result.append(combination[:])
            if it == len(nums):
                return
            
            for i in range(it, len(nums)):
                combination.append(nums[i])
                backtrack(i+1, combination)
                combination.pop()
            
        backtrack(it, combination)
        return result
            
