class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        next_grt = {nums2[0]: -1}
        st = [nums2[0]]
        
        for i in range(1, len(nums2)):
            next_grt[nums2[i]] = -1
            while (len(st) != 0) and (nums2[i] > st[-1]):
                next_grt[st[-1]] = nums2[i]
                st.pop()
            st.append(nums2[i])
        print(next_grt)
        res = [-1] * len(nums1)
        for i in range(0, len(nums1)):
            res[i] = next_grt[nums1[i]]
            
        return res
        
        