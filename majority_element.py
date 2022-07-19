class Solution(object):
    #Using sort
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        mid = int(len(nums)/2)
        return(nums[mid])
        
    #Booyer moore voting algorithm. 
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = None
        count = 0
        
        for num in nums:
            if count == 0: 
                result = num
            if num == result: 
                count += 1
            else:
                count -= 1

        return result
 
    