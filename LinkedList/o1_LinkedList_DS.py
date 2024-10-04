
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

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=", ")
            temp = temp.next

    def append(self,value):
        added_node = Node(value)
        if (self.head.value == self.tail.value) and (self.head.value is None):
            print(f"Linked list not have any element, creating new node")
            self.head = added_node
            self.tail = added_node
        else:
            # print(f"head : {self.head}")
            self.tail.next = added_node
            self.tail = added_node
        self.length= self.length+1
        return True

    def pop(self):
        print()
        # to remove last element from LL
        if (self.head.value == self.tail.value) and (self.head.value is None):
            print(f"Provided Linked list not have any element")
        elif (self.head.value == self.tail.value) and (self.length == 0):
            print(f"Provided Linked list have one element only")
            self.head = None
            self.tail = None
        else:
            print(f"Head At : {self.head.value}")
            # print(f"Tail At : {self.tail.value}")
            temp = self.head
            while temp != self.tail:
                lastNode= self.head
                # self.tail= self.head
                temp = self.head.next
                self.head = temp
                # print(f"Head At : {self.head.value}")
                # print(f"--Tail At : {self.tail.value}")
                print(f"--lastNode : {lastNode.value}")
            self.tail=lastNode


if __name__ == "__main__":
    my_LL = LinkedList(4)
    # print(my_LL.head.value)
    # print(my_LL.head.next)
    # my_LL.print_list()
    my_LL.append(10)
    my_LL.append(15)
    my_LL.append(25)
    my_LL.print_list()
    my_LL.pop()
    my_LL.print_list()
