# See chapter 6 CLSR - Introduction to Algorithms

class PriorityQueueADT:
    def __init__(self, A=[]):
        """
        Initializes the priority queue with an optional list A.
        """
        self.A = A  # The list representing the priority queue
        self.size = len(self.A)  # Size of the priority queue
        self._build_max_heap()  # Builds a max heap from the list

    def insert(self, x):
        """ 
        Inserts an element x into the priority queue.
        """
        self.size += 1  # Increment size
        self.A.append(None)  # Add a new element to the end of the list
        self._sift_up(self.size-1, x)  # Restore heap property by moving the new element up

    def extract_max(self):
        """ 
        Removes and returns the maximum element from the priority queue.
        """
        if self.is_empty():
            return None  # Return None if priority queue is empty
        
        max_item = self.A[0]  # Maximum element is at the root

        # Replace root with the last element and restore heap property
        self.A[0] = self.A[self.size - 1]
        self._sift_down(0)

        self.size -= 1  # Decrement size
        self.A.pop()  # Remove the last element

        return max_item

    def _build_max_heap(self):
        """
        Builds a max heap from the given list.
        """
        for i in range((self.size - 1) // 2, -1, -1):
            self._sift_down(i)  # Start from the last non-leaf node and heapify down

    def _sift_up(self, i, new_x):
        """
        Restores heap property by moving the element up.
        """
        self.A[i] = new_x
        while i > 0 and self.A[self._parent(i)] < self.A[i]:
            self._exchange(i, self._parent(i))
            i = self._parent(i)

    def _sift_down(self, i):
        """
        Restores heap property by moving the element down.
        """
        l = self._left(i)
        r = self._right(i)

        if l <= self.size - 1 and self.A[l] >= self.A[i]:
            largest = l
        else:
            largest = i
        
        if r <= self.size - 1 and self.A[r] >= self.A[largest]:
            largest = r

        if largest != i:
            self._exchange(i, largest)
            self._sift_down(largest)

    def is_empty(self):
        """
        Checks if the priority queue is empty.
        """
        return self.size == 0

    def _parent(self, i):
        """
        Returns the index of the parent of the node at index i.
        """
        return i // 2

    def _left(self, i):
        """
        Returns the index of the left child of the node at index i.
        """
        return 2*i

    def _right(self, i):
        """
        Returns the index of the right child of the node at index i.
        """
        return 2*i + 1
    
    def _exchange(self, i, largest):
        """
        Swaps elements at indices i and largest in the priority queue.
        """
        temp = self.A[i]
        self.A[i] = self.A[largest]
        self.A[largest] = temp

    
if __name__ == "__main__":
    # Example usage
    A = [2,7,26,25,19,17,1,90,3,36]
    pq1 = PriorityQueueADT(A)
    print(pq1.A)

    while not pq1.is_empty():
        print(pq1.extract_max())

    print(pq1.A)

    B = [(1, 'Riya'), (2, 'Abid'), (2, 'Harry', '123456'), (2, 'Stacy'),  (3, 'Charles')]
    pq2 = PriorityQueueADT(B)
    print(pq2.A)
    pq2.insert((3, "Sam"))

    while not pq2.is_empty():
        print(pq2.extract_max())
