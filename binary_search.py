class Solution(object):
    
    def binary_search(self, start_index, end_index, nums, target):
        if start_index <= end_index:
            mid = (start_index + end_index)//2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return self.binary_search(start_index, mid -1, nums, target)
            elif target > nums[mid]:
                return self.binary_search(mid + 1, end_index, nums, target)
        else:
            return -1
        
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        result = self.binary_search(0, len(nums)-1, nums, target)
        return result

