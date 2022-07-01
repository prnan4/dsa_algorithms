class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        set_distinct = set()
        for num in nums:
            if num in set_distinct: return True
            else: set_distinct.add(num)
        
        return False