class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        n = len(height)
        max_r = height[0]
        max_l = height[n-1]
        
        max_rights = [height[0]]
        max_lefts = [height[n-1]]
        
        prev_r = height[0]
        prev_l = height[n-1]
        
        for i in range(1, n):
            max_r = max(prev_r, max_r)
            max_rights.append(max_r)
            prev_r = height[i]
            
        for i in range(n- 2, -1, -1):
            max_l = max(prev_l, max_l)
            max_lefts.append(max_l)
            prev_l = height[i]
            
        max_lefts.reverse()
        
        res = 0
        for i in range(0, n):
            volume = min(max_rights[i] , max_lefts[i]) -  height[i]
            if volume > 0:
                res += volume
                
        return res
            
    