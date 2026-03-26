# in-class/MaxHeap.py

class MaxHeap:
    def __init__(self):
        self.heap = [] # Using a list as a C array here


    def get_parent_of(self, i: int):
        """Returns parent of element at `i`"""
        parent_index = (i - 1) // 2
        return self.heap[parent_index]

    
    def get_left_child_of(self, i: int):
        """Returns the left child element of `i`"""


    def get_right_child_of(self, i: int):
        """Returns the right child element of `i`"""


    def pop(self):
        """Returns the heap's root node"""


    def add(self, item):
        """Adds an item to the heap"""


    def __len__(self) -> int:
        return len(self.heap)