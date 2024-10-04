
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value=value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


if __name__ == "__main__":
    my_LL = LinkedList(4)
    print(my_LL.head.value)
    print(my_LL.head.next)
