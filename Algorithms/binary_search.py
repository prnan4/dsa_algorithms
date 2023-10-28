class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binary_search(nums, target, l, r):

            if r >= l:

                mid = (l + r ) //2 

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return binary_search(nums, target, mid + 1, r)
                else:
                    return binary_search(nums, target, l, mid-1)
            else:
                return -1


        return binary_search(nums, target, 0, len(nums)-1)