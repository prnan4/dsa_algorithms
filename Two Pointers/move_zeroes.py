class Solution(object):
    # Approach 1
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0:
            return nums

        first_zero = 0
        while (nums[first_zero] != 0):
            first_zero += 1

        if first_zero == len(nums):  
            return nums   

        for i in range(0, len(nums)):
            if first_zero < i and nums[i] != 0:
                temp = nums[i]
                nums[first_zero] = temp
                nums[i] = 0
                
                first_zero = 0
                while (nums[first_zero] != 0):
                    first_zero += 1

    # Optimized approach
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        first_zero = 0

        for i in range(0, len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[first_zero]
                nums[first_zero] = temp

                first_zero += 1
        