class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = 0
        mod_table = {0:1}
        prefixSum = 0
        for i in range(0, len(nums)):
            prefixSum += nums[i]

            if prefixSum % k in mod_table:
                res += mod_table[prefixSum % k]
                mod_table[prefixSum % k] += 1
            else:
                mod_table[prefixSum % k] = 1
        return res
        
    # Time limit exceeded
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        res = []

        for i in range(0, len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s % k == 0:
                    s = 0
                    res.append(nums[i:j+1])
        return len(res)