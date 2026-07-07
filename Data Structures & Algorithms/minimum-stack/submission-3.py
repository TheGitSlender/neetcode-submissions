class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.min_value) == 0:
            self.min_value.append(val)
        else:
            self.min_value.append(min(self.min_value[-1],val))

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_value[-1]
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]
