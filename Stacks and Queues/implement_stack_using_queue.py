#   Stack simulation
#
#   1   2   3   4 
#
#   Push operation -> O(1)
#   We use q.append() to add new element. This simulates the push operation in stack
#
#   1   2   3   4   5
#   ^               
#  Front              
#
#   Pop operation -> O(n)
#   We use q.append(q.popleft()) n-1 times and finally q.popleft() to remove the top element. This simulates stack
#   pop operation without using two queues and just using rotation operation
#
#   2   3   4   5   1 
#   3   4   5   1   2
#   4   5   1   2   3   
#   5   1   2   3   4
#   After O(n-1) times
#   1   2   3   4

class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

    def pop(self):
        """
        :rtype: int
        """
        n = len(self.st1)
        for i in range(n-1):
            self.st2.append(self.st1.pop())
        ele = self.st1.pop()
        for i in range(n-1):
            self.st1.append(self.st2.pop())
        return ele

    def peek(self):
        """
        :rtype: int
        """
        return self.st1[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.st1
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()