
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value, end=",")
            temp=temp.next
            
    def append(self,value):
        new_node = Node(value)
        # Edge case when Linked list is empty
        if (self.head is None):
            self.head = new_node
            self.tail = new_node
        else:
            # Here first need to define the new node        
            self.tail.next = new_node
            #second need to change the posion of tail pointer to new node
            self.tail = new_node
            self.length = self.length + 1
        return True
    
    def pop(self):
        # Edge case, if Linked list have no eliment
        if self.head is None:
            print(" Nothing to Pop")
            return None
        elif (self.head == self.tail) and self.length is 1:
            self.head = None
            self.tail = None
            return None
        else:
            tmp = self.head
            while tmp.next:
                lastNode = tmp
                tmp = tmp.next
                # print(f" value :{tmp.value}")               
            self.tail = lastNode
            self.tail.next = None
            self.length =self.length -1
        return tmp
    
    def prepend(self, value):
        new_node = Node(value=value)
        if self.length  is 0:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            return new_node
        else:
            # Basic approach
            # tmp = self.head
            # self.head = new_node            
            # self.head.next=tmp

            # Advanced Approach
            new_node.next= self.head
            self.head=new_node
            
            # increment the length
            self.length += 1
            return True
            
            



        


if __name__ == "__main__":
    ll = LinkedList(5)
    ll.append(10)
    ll.append(15)
    ll.append(11)
    ll.print_linked_list()
    print()
    poppedElemnet = ll.pop()    
    print(f"poped eliment : {poppedElemnet.value} Node:  {poppedElemnet}")
    poppedElemnet = ll.pop()    
    print(f"poped eliment : {poppedElemnet.value} Node:  {poppedElemnet}")
    poppedElemnet = ll.pop()    
    print(f"poped eliment : {poppedElemnet.value} Node:  {poppedElemnet}")
    # poppedElemnet = ll.pop()    
    # print(f"poped eliment : {poppedElemnet} Node:  {poppedElemnet}")
    ll.print_linked_list()
    print()
    ll.prepend(100)
    # ll.pop()
    ll.print_linked_list()
    print()
    ll.prepend(500)
    # ll.pop()
    ll.print_linked_list()
    print()


