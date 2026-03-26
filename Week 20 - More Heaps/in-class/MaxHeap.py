# in-class/MaxHeap.py

class MaxHeap:
    def __init__(self):
        self.heap = [] # Using a list as a C array here


    # Typically, in python, class methods starting with a double
    # underscore are intended to be "private". This is achieved by
    # the compiler prepending the class name in each such method name.
    # So `__get_parent_of()` can be externally accessed as
    # "MaxHeap__get_parent_of()".
    def __get_parent_of(self, i: int):
        """Returns parent of element at `i`"""
        parent_index = (i - 1) // 2
        return self.heap[parent_index]

    
    def __get_left_child_of(self, i: int):
        """Returns the left child element of `i`"""
        left_child_index = 2 * i + 1
        if left_child_index >= len(self.heap):
            return (left_child_index, None) # In case no left child exists
        return (left_child_index, self.heap[left_child_index])


    def __get_right_child_of(self, i: int):
        """Returns the right child element of `i`"""
        right_child_index = 2 * i + 2
        if right_child_index >= len(self.heap):
            return (right_child_index, None)
        return (right_child_index, self.heap[right_child_index])
    

    def __get_children_of(self, i: int):
        """Returns a 2-tuple containing both children (or None),
        in case any of those is absent"""
        left = self.__get_left_child_of(i)
        right = self.__get_right_child_of(i)
        return dict(left, right)


    def pop(self):
        """Returns the heap's root node"""
        root = self.pop(0) # Keep the root element somewhere
        last = self.heap.pop() # Get the last element
        self.heap.insert(0, last)
        current = 0
        children = self.__get_children_of(current)
        while any(child is not None and child > current for child in children.values()):
            max_child = max(children.items(), key=lambda pair: pair[1])
            # Swap max_child with current
            self.__swap(current, max_child[0])
            current = max_child[0]
            children = self.__get_children_of(current)
        return root

    
    def __swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


    def add(self, item):
        """Adds an item to the heap"""


    def __len__(self) -> int:
        return len(self.heap)