#   Queue simulation
#
#   1   2   3   4 
#
#   Push operation -> O(1)
#   We use st.append() to add new element. This simulates the push operation in stack
#
#   1   2   3   4   5
#                   ^
#                  Top
#
#   Pop operation -> O(n)
#   We use st.pop() n-1 times transferring the element to another stack. We then again transfer the moved elements to original stack.
#
#   st1 =   1   2   3   4   5
#   st2 =   []
#   
#   st1 =   1   2   3   4   5
#   st2 =   5
#   
#   st1 =   1   2   3 
#   st2 =   5   4 
#
#   st1 =   1   2   
#   st2 =   5   4   3
#
#   st1 =   1
#   st2 =   5   4   3   2
#
#   Pop st2
#   st2 =   5   4   3   2
#
#   st2 =   5   4   3
#   st1 =   2
#
#   st2 =   5   4   
#   st1 =   2   3
#
#   st2 =   5   
#   st1 =   2  3   4
#
#   st2 =   []
#   st1 =   2   3   4   5

class MyQueue(object):

    def __init__(self):
        self.st1 = []
        self.st2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.st1.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.st1[-1]
        

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