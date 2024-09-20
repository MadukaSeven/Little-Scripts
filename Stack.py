
class Stack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self,x:int):
        self.stack.append(x)

        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:

            popped = self.stack.pop()
            if popped == self.min_stack[-1]:
                self.min_stack.pop()
            return popped
        return None
