class Solution(object):
    
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binSearch(start, end, flag):
            if start <= end: 
                mid = (start + end) // 2
                if target == nums[mid]:
                    return mid
                elif target > nums[mid]:
                    return binSearch(mid + 1, end, 1)
                else: 
                    return binSearch(start, mid -1, 0)
            else:
                if flag == 1:
                    return start
                else:
                    return end + 1
        return binSearch(0, len(nums)-1, 0)
                
        