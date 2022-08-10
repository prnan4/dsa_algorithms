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
        