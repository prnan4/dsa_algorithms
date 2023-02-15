class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """

        number = 0
        multiplier = 1
        for i in range(len(num)-1, -1, -1):
            number += num[i]*multiplier 
            multiplier *= 10
        number += k 

        result = []
        while number != 0:
            result.append(number % 10)
            number = number // 10
        return result[::-1]
