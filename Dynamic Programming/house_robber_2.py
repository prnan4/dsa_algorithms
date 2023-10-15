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

    # ========================== APPROACH 3 ==========================
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
    
    # ========================== APPROACH 4 ==========================
    # Bottom up DP
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem1 = [None] * (len(nums) - 1)
        mem2 = [None] * (len(nums) - 1)

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        mem1[0] = nums[0]
        mem1[1] = max(nums[0], nums[1])

        mem2[0] = nums[1]
        mem2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            mem1[i] = max(nums[i] + mem1[i-2], mem1[i-1])
        for j in range(3, len(nums)):
            i = j-1
            mem2[i] = max(nums[j] + mem2[i-2], mem2[i-1])

        return max(mem1[len(nums)-2], mem2[len(nums)-2])

