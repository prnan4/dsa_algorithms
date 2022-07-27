class Solution(object):

    # Using monotonic stack
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        
        output = [0] * len(temperatures)
        stack = [[temperatures[0], 0]]
        
        for i in range(1, len(temperatures)):
            while stack and (temperatures[i] > stack[-1][0]):
                daysToWait = i - stack[-1][1]
                output[stack[-1][1]] = daysToWait
                stack.pop()
            stack.append([temperatures[i], i])
        return output
                
            