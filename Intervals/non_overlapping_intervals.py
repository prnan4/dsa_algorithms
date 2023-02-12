class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] < res[-1][1]:
                if curr[1] >= res[-1][1]:
                    continue
                else:
                    res.pop()
                    res.append(curr)
            else:
                res.append(curr)
        return len(intervals) - len(res)