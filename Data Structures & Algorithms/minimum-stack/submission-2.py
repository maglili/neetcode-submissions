class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        cur_min = self.getMin() if len(self.minstack) > 0 else None
        new_min = val if cur_min == None else min(val, cur_min)
        self.minstack.append(new_min)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
