# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersionIterative(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        end = n - 1
        while start < end:
            mid = (end + start) // 2
            if isBadVersion(mid+1):
                end = mid
            else:
                start = mid + 1
        return start + 1
        
    def firstBadVersionRecursive(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        def findBadVersion(start, end):
            if start == end: 
                return start + 1
            mid = (end + start) // 2
            if isBadVersion(mid+1):
                return findBadVersion(start, mid)
            else:
                return findBadVersion(mid + 1, end)
        
        return findBadVersion(0, n-1)