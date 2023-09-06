class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        mem = [0] *(n+1)
        for i in range(1, n+1):
            if i & (i-1) == 0:
                val = i
            mem[i] = 1 + mem[i % val]
        return mem


