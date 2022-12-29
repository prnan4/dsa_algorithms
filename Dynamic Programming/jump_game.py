class Solution(object):

    # ========================== APPROACH 1 ==========================
    # Recursion without memoization 
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def canJumpfromi(i):
            if i == len(nums) - 1:
                return True

            result = False
            for j in range(1, nums[i] + 1):
                result = result or canJumpfromi(i+j)
            return result
        
        return canJumpfromi(0)

    # ========================== APPROACH 2 ==========================
    # Recursion with memoization
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        memory = [None for _ in range(len(nums))]
        memory[-1] = True
        
        def canJumpfromi(i):
            if memory[i]:
                return memory[i]
            
            result = False
            for j in range(1, nums[i] + 1):
                result = result or canJumpfromi(i+j)
            memory[i] = result
            return memory[i]
        
        return canJumpfromi(0)


    # ========================== APPROACH 3 ==========================
    # Bottom up DP - still TLE
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        n = len(nums)
        memory = [False for _ in range(n)]
        memory[-1] = True

        for i in range(n-2, -1, -1):
            for j in range(1, nums[i] +1):
                if (i + j < n) and memory[i+j] is True:
                    memory[i] = True
                    break

        return memory[0]

    # ========================== APPROACH 4 ==========================
    # Bottom up DP - optimised
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
      
        n = len(nums)
        memory = [False for _ in range(n)]
        memory[-1] = True

        for i in range(n-2, -1, -1):
            for j in range(1, min(n-i, nums[i] +1 )):
                if memory[i+j] is True:
                    memory[i] = True
                    break

        return memory[0]
    """
    Refered from:
    def canJump(self, nums):
      
        n = len(nums)
        memory = [False for _ in range(n)]
        memory[-1] = True

        for i in range(n-2, -1, -1):
            for j in range(i+1, min(n, i+nums[i]+1)):
                if memory[j] is True:
                    memory[i] = True
                    break

        return memory[0]
    """