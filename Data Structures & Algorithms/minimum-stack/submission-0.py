class MinStack:
    # brute force solution
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        minNum = self.stack[0]
        for num in self.stack:
            minNum = min(minNum, num)
        
        return minNum

