class Solution(object):
    #========================== APPROACH 1 ==========================  
    # Only 5% faster. Updating result array, by adding new element and removing the last added element.

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        for i in range(0, len(intervals)):
            if result and (intervals[i][0] <= result[-1][1]):       
                result.append([result[-1][0], max(intervals[i][1], result[-1][1])])
                result.pop(-2)
            else:
                result.append([intervals[i][0], intervals[i][1]])
        return result

    #========================== APPROACH 1 ==========================  
    # 90% faster. Updating last added element to result array directly.

    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        result = []
        for i in range(0, len(intervals)):
            if result and (intervals[i][0] <= result[-1][1]):       
                result[-1][1] =  max(intervals[i][1], result[-1][1])
            else:
                result.append([intervals[i][0], intervals[i][1]])
        return result