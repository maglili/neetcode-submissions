class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for p, s in sorted(zip(position, speed))[::-1]:
            t = (target - p) / s
            stack.append(t)

            if len(stack) >= 2 and t <= stack[-2]:
                stack.pop()

        return len(stack)
