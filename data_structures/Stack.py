# LIFO structure
class Stack:

    def __init__(self):
        self.stack = []
        self.is_empty = self.stack == []

    def __len__(self):
        return len(self.stack)

    # O(1)
    def push(self, data):
        self.stack.append(data)
    # O(1)
    def pop(self):
        if self.stack_size() < 1:
            return
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    # def is_empty(self):
    #     return self.stack == []

    def stack_size(self):
        return len(self.stack)

stack  = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(f'Size: {stack.stack_size()}')
print(f'Popped item: {stack.pop()}')
print(f'Size: {stack.stack_size()}')
print(f'Peek last item: {stack.peek()}')
print(f'Size: {stack.stack_size()}')