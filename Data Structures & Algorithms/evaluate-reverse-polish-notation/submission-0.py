class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rslt = 0
        stack = []
        for char in tokens:
            if char.isnumeric():
                stack.append(char)
            else:
                temp = 0
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
                rslt = temp
        return rslt
                

                