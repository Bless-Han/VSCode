class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None

    def min(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return None

minStack = MinStack()
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
assert minStack.min() == -3
minStack.pop()
assert minStack.top() == 0
assert minStack.min() == -2

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
