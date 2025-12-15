# Linked list implementation in Python

class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0
        
    def create(self, X):                        # O(n)
        for item in reversed(X):
            self.insert_first(item)

    def insert_first(self, x):                  # O(1)
        new_node = Node(x)                      # create a new node with item x
        new_node.next = self.head               # set the new node to point to the current head
        self.head = new_node                    # replace the linked list head to be new node
        self._size += 1                         # increase the size

    def insert_last(self, x):                   # O(n)
        current_node = self.head                # set current node to head
        # find the last node 
        while current_node.next != None:        # while the current node isn' the last node
            current_node = current_node.next    # set current node to next node
        new_node = Node(x)                      # create new node
        current_node.next = new_node            # set the last_node to point to new node
        
    def get_at(self, i):                        # O(n) - worse case, actually takes O(i)
        current_node = self.head                # set current node to head
        # find the ith node 
        j = 0
        while j != i:                           # while we are not at the ith node
            current_node = current_node.next    # set current node to next node
            j += 1
        return current_node.item 
        
        

if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.insert_first(1)
    linked_list.insert_first(2)
    linked_list.insert_first(3)
    
    linked_list.insert_last(4)
    
    linked_list2 = LinkedList()
    linked_list2.create([1,2,3,4])
    print(linked_list2.get_at(0))
    print(linked_list2.get_at(1))
    print(linked_list2.get_at(2))
    print(linked_list2.get_at(3))
    
