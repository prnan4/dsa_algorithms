class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dict_map = {}
        len_longestSequence = 0
        for n in nums:
            if n not in dict_map:
                if (n-1) in dict_map:
                    l = dict_map[n-1]
                else:
                    l = 0
                if (n+1) in dict_map:
                    r = dict_map[n+1]
                else:
                    r = 0
                    
                res = l + r + 1
                
                dict_map[n] = res
                dict_map[n-l] = res
                dict_map[n+r] = res
                len_longestSequence = max(res, len_longestSequence )

            else:
                continue
            
        return len_longestSequence 
        