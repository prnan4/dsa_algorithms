class Solution(object):
    #Kadane's algorithm
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        subarray_sum = nums[0]
        max_sum = nums[0]
        
        for num in nums[1:]:
            if subarray_sum < 0:
                subarray_sum = num
            else:
                subarray_sum += num
            max_sum = max(max_sum, subarray_sum)
            
        return max_sum
        