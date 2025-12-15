# Linked list implementation in Python

class Node:
    # Creating a node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return "Node : {0}".format(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None        # store head node
        self.tail = None        # store tail node
        self._size = 0

    def __str__(self):                      # pretty print of the linked list
        current_node = self.head
        output = []
        while current_node != None:
            output.append(str(current_node))
            current_node = current_node.next

        if output:
            return " -> ".join(output)
        else:
            return "Empty List"
        
    def create(self, X):                                    # O(n)
        for data in reversed(X):
            self.insert_first(data)

    def insert_first(self, x):                              # O(1)
        new_head = Node(x)                                  # create a new node with item x
        self._size += 1                                     # increase the size
        if self.head == None and self.tail == None:         # edge case - no head or tail
            self.head = new_head
            self.tail = new_head
            # exit here
            return
        
        self.head.prev = new_head               # set the head previous pointer to point to new head
        new_head.next = self.head               # set the new heads next pointer to point to the current head
        self.head = new_head                    # replace the old head with the new head
        

    def insert_last(self, x):                           # O(1)
        if self._size == 0:
            self.insert_first(x)
            return

        new_tail = Node(x)                              # create a new node with item x
        self._size += 1   

        self.tail.next = new_tail                       # set the tails next to new tail
        new_tail.prev = self.tail                       # set the new tails previous to old tail
        self.tail = new_tail                            # replace the old tail with the new tail
        
    def get_at(self, i):                        # O(n) - worse case, actually takes O(i)
        current_node = self.head                # set current node to head
        # find the ith node 
        j = 0
        while j != i:                           # while we are not at the ith node
            current_node = current_node.next    # set current node to next node
            j += 1
        return current_node.data 
    
    def set_at(self, i, x):                     # O(n) - worse case, actually takes O(i)
        current_node = self.head                # set current node to head
        # find the ith node 
        j = 0
        while j != i:                           # while we are not at the ith node
            current_node = current_node.next    # set current node to next node
            j += 1
        current_node.data = x

    def delete_first(self):                                 # O(1)
        if self.head == None:                               # edge case, no head
            print("Empty list, cannot delete first node")
            return 
        
        self._size -= 1                                     # decrease size by 1
        
        if self.head.next == None:                          # edge case - 1 node
            self.head = None
            self.tail = None
            return 
        
        new_head = self.head.next                           # set new_head to next node from head
        self.head = new_head                                # replace old head with new head
        self.head.prev = None                               # set new head previous pointer to None

    def delete_last(self):                                  # O(1)
        if self.tail == None:                               # edge case - no tail
            print("Empty list, cannot delete last node")
            return 
        
        if self._size == 1:
            self.delete_first()
            return
        
        self._size -= 1                                     # decrease size by 1
                
        self.tail = self.tail.prev                          # replace tail with second to last node        
        self.tail.next = None                               # set tails next pointer to none

    def size(self):
        return self._size
        
 
if __name__ == '__main__':

    linked_list = DoublyLinkedList()

    # Assign item values
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    linked_list.insert_first(3)
    
    linked_list.insert_last(4)
    
    print(linked_list)

    linked_list.delete_first()
    print(linked_list)
    linked_list.delete_last()
    print(linked_list)
    linked_list.delete_first()
    linked_list.delete_first()
    linked_list.delete_first()
    print(linked_list)
    linked_list.insert_last("Sam")
    print(linked_list)
    linked_list.delete_last()
    print(linked_list)
    linked_list.delete_first()
    print(linked_list)
    linked_list.delete_last()
    print(linked_list)
