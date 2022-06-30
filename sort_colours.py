class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = {0:0, 1:0, 2:0}
        for num in nums:
            if num is 0: count[0] += 1
            elif num is 1: count[1] += 1
            else: count[2] += 1
        index = 0
        while count[0] > 0:
            nums[index] = 0
            count[0] -= 1
            index += 1
            
        while count[1] > 0:
            nums[index] = 1
            count[1] -= 1
            index += 1
            
        while count[2] > 0:
            nums[index] = 2
            count[2] -= 1
            index += 1
            
        return nums
    
    def sortColorsDutchNationalAlgorithm(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        low = mid = 0
        high = len(nums) - 1
        
        def swap(a, b):
            temp = a
            a = b
            b = temp
            return a, b
            
        while mid <= high:
            if nums[mid] is 0:
                nums[mid], nums[low] = swap(nums[mid], nums[low])
                mid += 1
                low += 1
            elif nums[mid] is 1:
                mid += 1
            else:
                nums[mid], nums[high] = swap(nums[mid], nums[high])
                high -= 1
        return nums


                