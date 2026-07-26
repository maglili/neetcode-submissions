class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '[({':
                stack.append(char)
            else:
                l_char = stack.pop()
                if ((l_char == '[') and (char != ']')\
                or ((l_char == '(') and (char != ')'))\
                or ((l_char == '{') and (char != '}'))):
                    return False
        return True
                
        