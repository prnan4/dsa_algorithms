class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        
        while len(nums) >= 3:
            i= nums.pop(0)
            value_to_match = 0 - i
            match_dict = {}
            for j in nums:
                if j in match_dict:
                    if [i, match_dict[j], j] not in result:
                        result.append([i, match_dict[j], j])
                    del match_dict[j]
                else:
                    match_dict[value_to_match - j] = j
        return result
                    