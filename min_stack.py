class MinStack(object):

    def __init__(self):
        self.elements = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        stack = self.elements
        if not stack: 
            currentMin = val
        else: 
            if val < stack[-1][1]: 
                currentMin = val
            else:
                currentMin = stack[-1][1]
        stack.append([val, currentMin])
        

    def pop(self):
        """
        :rtype: None
        """
        stack = self.elements
        stack.pop()

    def top(self):
        """
        :rtype: int
        """
        stack = self.elements
        return stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        stack = self.elements
        return stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()