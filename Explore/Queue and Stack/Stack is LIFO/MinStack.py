# time: O(1) for each operation
# space: O(n) for the stack (max 2N if every operation is a push)
class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
        else:
            curr_min = self.stack[-1][-1]
            self.stack.append((val, min(val, curr_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][-1]
