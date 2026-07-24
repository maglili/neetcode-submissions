class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if not stack:
                    return False
                last = stack.pop()
                target = last + c
                if target not in ["()", "{}", "[]"]:
                    return False
        return True if len(stack) == 0 else False
