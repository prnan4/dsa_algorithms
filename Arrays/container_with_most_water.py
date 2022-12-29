class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        if (not height) or (len(height) == 1): return max_area
        
        left = 0
        right = len(height) - 1
        while right > left:
            w = right - left
            h = min(height[left], height[right])
            area = w * h
            if area > max_area: max_area = area
                
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1
                
        return max_area