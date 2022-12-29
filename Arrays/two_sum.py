class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr_dict = {}
        for i, num in enumerate(nums):
            arr_dict[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if (diff in arr_dict) and (i != arr_dict[diff]):
                return[i, arr_dict[diff]]