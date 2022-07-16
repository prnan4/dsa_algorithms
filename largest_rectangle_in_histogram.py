class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        left = [0]* len(heights)
        right = [0]* len(heights)
        left[0] = -1
        right[len(heights) - 1] = len(heights)
        
        for i in range(1, len(heights)):
            p = i-1
            while (p >= 0 and heights[p] >= heights[i]):
                p = left[p]
            left[i] = p
            
        print(left)
        for i in range(len(heights)-2, -1, -1):
            p = i+1
            while (p < len(heights) and heights[p] >=heights[i]):
                p = right[p]
            right[i] = p
        
        max_area = 0      
        for i in range(0, len(heights)):
            max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))

        return max_area
            
        
        