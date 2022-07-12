class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        
        def arithmeticOperations(num1, num2, operator):
            if operator == '+':
                return num1 + num2
            if operator == '-':
                return num1 - num2
            if operator == '*':
                return num1 * num2
            if operator == '/':
                return int(num1/num2)
            
        for token in tokens:
            if token[0] == '-' and len(token) > 1:
                if token[1:].isdigit():
                    stack.append(int(token))
            elif token.isdigit():
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = arithmeticOperations(num1, num2, token)
                stack.append(res)
               
        return stack[0]
                
                
        