class Solution(object):
    # ========================== APPROACH 1 ==========================
    # Recursion without memoization
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        originalLength = len(nums)
        def maxAmount(nums, flag):
            n = len(nums)
            # Base condition
            if n == 0:
                return 0
            if n == 1 and flag is True:
                return 0

            if n == originalLength:
                return max(nums[n-1] + maxAmount(nums[:-2], True), maxAmount(nums[:-1], False))

            else:
                return max(nums[n-1] + maxAmount(nums[:-2], flag), maxAmount(nums[:-1], flag))
              
        return maxAmount(nums, False)

    # ========================== APPROACH 2 ==========================
    # Recursion with memoization
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        originalLength = len(nums)
        
        #i index is for flag value False. Second index is for flag value True.
        memory = [[None, None] for _ in range(originalLength+1)]
        memory[0][0] = 0
        memory[0][1] = 0
        memory[1][1] = 0
        
        def maxAmount(nums, flag):
            n = len(nums)
            if memory[n][flag] is not None:
                return memory[n][flag]
            
            if n == originalLength:
                memory[n][flag] = max(nums[n-1] + maxAmount(nums[:-2], 1), maxAmount(nums[:-1], 0))

            else:
                memory[n][flag] = max(nums[n-1] + maxAmount(nums[:-2], flag), maxAmount(nums[:-1], flag))
            return memory[n][flag]
              
        return maxAmount(nums, 0)

    # ========================== APPROACH 2 ==========================
    # Bottom UP DP
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [[None, None] for _ in range(len(nums)+ 1)]
        
        memory[0][0] = 0
        memory[0][1] = 0
        memory[1][1] = 0
        memory[1][0] = nums[0]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        for i in range(2, n+1):
            for j in range(0, 2):
                if i == n:
                    memory[i][j] = max(nums[i-1] + memory[i-2][1], memory[i-1][0])
                else:
                    memory[i][j] = max(nums[i-1] + memory[i-2][j], memory[i-1][j])

        return max(memory[n][0], memory[n][1])