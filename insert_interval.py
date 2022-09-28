class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        newInterval_added = False
        
        def merge_interval(interval):
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
                
        for interval in intervals:
            if not newInterval_added:
                if newInterval[0] <= interval[0]:
                    merge_interval(newInterval)
                    newInterval_added = True
                    merge_interval(interval)
                else:
                     result.append(interval)
            else:
                merge_interval(interval)
        
        if not newInterval_added:
            merge_interval(newInterval)
        
        return result
        