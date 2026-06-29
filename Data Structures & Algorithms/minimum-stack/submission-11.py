class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    # O(1) now!
    def getMin(self) -> int:
        # print(self.stack)
        # print("min")
        # print(self.minStack)
        # print(self.minStack[-1])
        # print("===")
        return self.minStack[-1]

