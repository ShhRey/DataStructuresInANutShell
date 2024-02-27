class Stack:
    def __init__(self, size):
        self.size = size
        self.container = [None] * size
        self.t = -1  # Top of stack

    def _push(self, item):
        if self._isfull():
            print("Stack Overflow")
            return
        self.t += 1
        self.container[self.t] = item

    def _pop(self):
        if self._isempty():
            print("Stack Underflow")
            return None
        item = self.container[self.t]
        self.container[self.t] = None
        self.t -= 1
        return item

    def _isempty(self):
        return self.t == -1

    def _isfull(self):
        return self.t == self.size - 1


# Example usage:
stack = Stack(5)

# Pushing elements onto the stack
stack._push(1)
stack._push(2)
stack._push(3)
stack._push(4)
stack._push(5)

# Trying to push more elements than the stack size
stack._push(6)

# Popping elements from the stack
print(stack._pop())
print(stack._pop())
print(stack._pop())
print(stack._pop())
print(stack._pop())

# Trying to pop more elements than the stack contains
print(stack._pop())
