class Solution(object):
    # ========================== APPROACH 1 ==========================  
    # O(n^2) complexity. Time limit exceeded
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        answer = [1] * n
        
        for i in range(0, n):
            for j in range(0, n):
                if i == j:
                    continue
                answer[j] *= nums[i]
                
        return answer
        
    # ========================== APPROACH 2 ==========================  
    # Second optimized, for three loops
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n
        right = [1] * n
        
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
            print(left[i])
        for i in range(n - 2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        for i in range(0, n):
            left[i] *= right[i]
        
        return left

    # ========================== APPROACH 3 ==========================  
    # Best optimised
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        right = 1
        
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]
        for i in range(n - 1, -1, -1):
            ans[i] *= right
            right *= nums[i]
        return ans
    
    # Oct 15, 2023


    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = [1] * len(nums)
        prodRight = [1] * len(nums)
        prodLeft = [1] * len(nums)

        for i in range(1, len(nums)):
            prodRight[i] = prodRight[i-1] * nums[i-1]
        result[len(nums) - 1] = prodRight[len(nums)-1]

        for i in range(len(nums)-2, -1, -1):
            prodLeft[i] = prodLeft[i+1] * nums[i+1]
            result[i] = prodLeft[i] * prodRight[i]
        
        return result