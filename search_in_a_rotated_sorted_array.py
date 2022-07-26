class Solution(object):
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        def binarySearch(start, end):
            if start <= end:
                mid = (start + end) // 2
                if nums[mid] == target: 
                    return mid

                # Implies array in left side of mid is sorted
                if nums[start] <= nums[mid]:

                    # Target is in the sorted array in left side of mid
                    if nums[start] <= target < nums[mid]:
                        return binarySearch(start, mid - 1)

                    # Target is in the unsorted array in right side of mid
                    else:
                        return binarySearch(mid + 1, end)

                # Implies array in right side of mid is sorted
                else:

                    # Target is in the sorted array in right side of mid
                    if nums[mid] < target <= nums[end]:
                        return binarySearch(mid + 1, end)

                    # Target is in the unsorted array in right side of mid
                    else:
                        return binarySearch(start, mid -1)
                
            else: 
                return -1
                    
            
        return binarySearch(0, len(nums)-1)