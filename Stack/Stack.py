class Stack:
    def __init__(self):
        self.stack = list()

    def push(self, item):
        print(f"Available eliment in Stack: {self.stack}")
        self.stack.append(item)
        print(f"Element pushed to Stack: {self.stack}")

    def pop(self):
        print(f"Available eliment in Stack: {self.stack}")
        if len(self.stack) == 0:
            raise IndexError("Pop from empty Stack")
        else:
            item = self.stack.pop()
            print(f"Remaming Stack: {self.stack}")
            print(f" Poped Eliment : {item}")
            return item

    def peek(self):
        if len(self.stack) == 0:
            raise IndexError("empty Stack")
        else:
            item = self.stack[-1]
            print(f"Remaming Stack: {self.stack}")
            print(f" Peek Eliment : {item}")
            return item 
    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)
