class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        set_sums = {0: 1}

        res = 0
        prefixSum = 0

        for i in range(0, len(nums)):
            prefixSum += nums[i]
            print(prefixSum)

            if prefixSum - k in set_sums:
                res += set_sums[prefixSum - k]

            
            if prefixSum in set_sums:
                set_sums[prefixSum] += 1
            else:
                set_sums[prefixSum] = 1
        print(set_sums)
        return res