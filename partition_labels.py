class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        ch_map = {}
        for i, ch in enumerate(s):
            if ch in ch_map:
                ch_map[ch][1] = i
            else:
                ch_map[ch] = [i, i]
                
        intervals = []
        for pair in ch_map.values():
            intervals.append(pair)
        
        intervals = sorted(intervals, key=lambda x: x[0])

        i = 0
        j = 0
        res = []
        print(intervals)
        while i < len(intervals):
            end = intervals[i][1]
            st = intervals[i][0]
            j = i+1
            length = end - st + 1
        
            while j < len(intervals) and intervals[j][0] < end:
                
                if intervals[j][1] > end:
                    end = intervals[j][1]
                length = end - st + 1
                j += 1
                
            i = j 
            res.append(length)
            
        return res
        