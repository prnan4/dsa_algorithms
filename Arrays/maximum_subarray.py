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

    # Dec 26, 2022 revision
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_tot = float('-inf')

        total = 0
        for ele in nums:
            total += ele
            if total > max_tot:
                max_tot = total
            if total < 0:
                total = 0
        return max_tot

        