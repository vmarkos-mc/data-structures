# Linked list implementation in Python
# Programiz https://www.programiz.com/dsa/linked-list

class Node:
    """ Represents a single node"""
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    """ The whole linked list"""
    def __init__(self):
        self.head = None

if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    current_node = linked_list.head                # set current node to head
    # find the last node 
    while current_node.next != None:        # while the current node isn' the last node
        print(current_node.item)
        current_node = current_node.next    # set current node to next node
    print(current_node.item)                # print the last node