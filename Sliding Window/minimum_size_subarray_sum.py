class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        right = 0
        left = 0
        res = float('inf')

        subarray_sum = nums[0]
        while right < len(nums) -1:
            print(left, right, subarray_sum, res)
            if subarray_sum >= target:
                res = min(res, right - left +1)
                subarray_sum -= nums[left]
                left += 1
            else:
                right += 1
                subarray_sum += nums[right]
                

        while left <= right:
            if subarray_sum >= target:
                    res = min(res, right - left +1)
                    subarray_sum -= nums[left]
                    left += 1
            else:
                break

        if res ==  float('inf'):
            return 0
        return res