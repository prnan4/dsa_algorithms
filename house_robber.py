class Solution(object):
    # ========================== APPROACH 1 ==========================
    # Recursion without memoization
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def maxAmount(nums):
            # Exit condition
            if not nums:
                return 0
            
            n = len(nums)
            # Note: You don't have to handle edge case n == 1, seperately. nums[:-2] for n == 1 will still yield an empty array.
            return max(nums[n-1] + maxAmount(nums[:-2]), maxAmount(nums[:-1]))
            
        return maxAmount(nums)

    # ========================== APPROACH 2 ==========================
    # Recursion with memoization
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [None for _ in range(len(nums))]
        
        def maxAmount(nums):
            # Exit condition
            if not nums:
                return 0

            n = len(nums)
            if memory[n-1] is not None:
                return memory[n-1]
            
            # Note: You don't have to handle edge case n == 1, seperately. nums[:-2] for n == 1 will still yield an empty array.
            memory[n-1] = max(nums[n-1] + maxAmount(nums[:-2]), maxAmount(nums[:-1]))
            return memory[n-1]
        
        return maxAmount(nums)

    # ========================== APPROACH 3 ==========================
    # Bottom Up DP
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [None for _ in range(len(nums))]
        memory[0] = nums[0]
        
        for i in range(1, len(memory)):
            if i >= 2:
                memory[i] = max(nums[i] + memory[i-2], memory[i-1])
            else:
                memory[i] = max(nums[i], memory[i-1])
        return memory[len(nums) - 1]
            