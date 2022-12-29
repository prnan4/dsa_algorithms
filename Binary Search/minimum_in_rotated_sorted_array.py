class Solution(object):
    # Approach 1 
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        def binary_approach(start, end):
            mid = (start+end)/2
            
            if mid == start:
                if nums[start] < nums[end]:
                    return nums[start]
                else:
                    return nums[end]
                
            elif nums[mid] > nums[end]:
                return binary_approach(mid, end)
            
            else:
                return binary_approach(start, mid)
                
            
        return binary_approach(0, len(nums)-1)


    # Optimised approach
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if nums[len(nums) -1] >= nums[0]:
            return nums[0]
        
        def binary_approach(start, end):
            mid = (start+end)/2
            
            if nums[mid] > nums[mid+1]:
                return nums[mid+1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid] > nums[end]:
                return binary_approach(mid + 1, end)
            else:
                return binary_approach(start, mid -1)
           
        return binary_approach(0, len(nums)-1)
    
    


        