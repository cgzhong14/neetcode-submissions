class MinStack:

    def __init__(self):
        self.stack = []
        # [0,1,2,3]

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) != 0:
            return self.stack[-1]

    def getMin(self) -> int:
        minimum = float('inf')
        if len(self.stack) != 0:
            for i in self.stack:
                minimum = min(minimum,i)
        return minimum