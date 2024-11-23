

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        tmp = self.top
        while tmp:
            print(tmp.value)
            tmp = tmp.next

if __name__ == "__main__":
    stackDs = Stack(4)
    stackDs.print_stack()
