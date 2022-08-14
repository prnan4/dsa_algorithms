class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        prev_sum_digits = set()
        
        while(n != 1):
            if n in prev_sum_digits:
                return False
            prev_sum_digits.add(n)
            sum_digits = 0
            while(n != 0):
                sum_digits += (n % 10) * (n % 10)
                n = n // 10
            n = sum_digits
        
        return True