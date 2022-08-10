class Solution(object):
    # ========================== APPROACH 1 ==========================
    # Recursion without memoization. Time limit exceeded.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def maxIncSeq(prev, i):
            
            if i == len(nums):
                return 0
            
            dont_take = maxIncSeq(prev, i+1)
            if (prev == -1) or (nums[i] > nums[prev]):
                take = 1 + maxIncSeq(i, i+1)
            else:
                take = 0
            return max(take, dont_take)

        return maxIncSeq(-1, 0)
        
    # ========================== APPROACH 1 ==========================
    # Recursion with memoization. 2D Memory is used. Still time limit exceeded.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [[None for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        for i in range(len(nums) + 1):
            memory[i][len(nums)] = 0
            
        def maxIncSeq(prev, i):
            
            if i == len(nums):
                return 0
            if memory[prev+1][i] is not None:
                return memory[prev+1][i]
            
            dont_take = maxIncSeq(prev, i+1)
            if (prev == -1) or (nums[i] > nums[prev]):
                take = 1 + maxIncSeq(i, i+1)
            else:
                take = 0
            memory[prev+1][i] = max(take, dont_take)
            return memory[prev+1][i] 

        return maxIncSeq(-1, 0)

    # ========================== APPROACH 3 ==========================
    # Recursion with memoization. 1D Memory is used. Still time limit exceeded.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memory = [None for _ in range(len(nums)+1)] 
        memory[len(nums)] = 0
            
        def maxIncSeq(prev, i):
            
            if i == len(nums):
                return 0
            if memory[prev+1] is not None:
                return memory[prev+1]
            
            dont_take = maxIncSeq(prev, i+1)
            if (prev == -1) or (nums[i] > nums[prev]):
                take = 1 + maxIncSeq(i, i+1)
            else:
                take = 0
            memory[prev+1]= max(take, dont_take)
            return memory[prev+1]

        return maxIncSeq(-1, 0)

    # ========================== APPROACH 4 ==========================
    # Bottom up DP. For every element, check the longest increasing sequence that can be formed.
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [1 for _ in range(n)] 
        
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        max_seq = 1
        for k in range(n):
            max_seq = max(max_seq, dp[k])
        return max_seq
        
        
        
        