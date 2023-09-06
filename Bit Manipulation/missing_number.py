class Solution(object):
    # Approach 1
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        if nums[0] != 0:
            return 0
        elif nums[n-1] != n:
            return n
        else:
            for i in range(1, n):
                if nums[i] != i:
                    return i
        
    # Approach 2
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        for i in range(len(nums)+1):
            if i not in nums:
                return i
    # Approach 3       
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = len(nums)
        for i in range(len(nums)):
            xor ^= i ^ nums[i]
        return xor

