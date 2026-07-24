class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char.lstrip('-').isnumeric():
                stack.append(char)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                if char == '+':
                    temp = num1 + num2
                elif char == '-':
                    temp = num1 - num2
                elif char == '*':
                    temp =  num1 * num2
                else:
                    temp = int(num1 / num2)
                stack.append(temp)
        return int(stack[0])
                

                