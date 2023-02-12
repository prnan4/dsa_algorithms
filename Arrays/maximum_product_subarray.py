class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_val = nums[0]
        min_val = nums[0]
        res = max_val
        for i in range(1, len(nums)):
            curr = nums[i]

            temp = max(curr, max_val*curr, min_val*curr)
            min_val = min(curr, max_val*curr, min_val*curr)

            max_val = temp
            res = max(max_val, res)

        return res
