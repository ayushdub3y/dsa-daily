class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack =[]
        self.minimum = float('inf')
    def push(self, value):
        self.stack.append(value)
        if not self.minStack:
            self.minStack.append(value)
        else:
            self.minStack.append(min(value, self.minStack[-1]))
    def pop(self):
        self.minStack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def getMin(self):
        return self.minStack[-1]