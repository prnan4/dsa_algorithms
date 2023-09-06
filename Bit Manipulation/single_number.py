class Solution(object):
    # Approach 1
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        unique_nums = set()
        for num in nums:
            if num in unique_nums:
                unique_nums.remove(num)
            else:
                unique_nums.add(num)
        return list(unique_nums)[0]
    
    # Approach 2
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor