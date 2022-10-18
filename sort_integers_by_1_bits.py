# Tested in Goldman Sachs coding assesment

class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        def count_ones(n):
            count = 0
            while(n):
                count += n & 1
                n = n >> 1
            return count
        
        count_dict = {}
        for i in arr:
            ones = count_ones(i)
            if ones in count_dict:
                count_dict[ones].append(i)
            else:
                count_dict[ones] = [i]
                
        result = []
        for i in sorted(count_dict.keys()):
            result.extend(sorted(count_dict[i]))  
            
        return result
        
        