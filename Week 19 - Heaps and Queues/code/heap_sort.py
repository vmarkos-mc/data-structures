# This code performs heap sort on a given list A.

def heap_sort(A):
    # build A as a heap
    heap_size = len(A)
    build_max_heap(A)  # Convert the list into a max heap
    # iterate over the heap backwards
    for i in range(len(A) - 1, 0, -1):
        # swap the first item and item i, item i is now sorted
        exchange(A, 0, i)  # Move the maximum element to its correct position
        heap_size -= 1  # Decrease heap size as the maximum element is in its final position
        max_heapify(A, heap_size, 0)  # Restore heap property

def build_max_heap(A):
    """
    Builds a max heap from the given list.
    """
    for i in range((len(A) - 1)//2, -1, -1):
        max_heapify(A, len(A), i)  # Start from the last non-leaf node and heapify down

def max_heapify(A, size, i):
    """ 
    Restores heap property by moving the element down.
    """
    l = left(i)
    r = right(i)

    if l <= size - 1 and A[l] >= A[i]:
        largest = l
    else:
        largest = i
    
    if r <= size - 1 and A[r] >= A[largest]:
        largest = r

    if largest != i:
        exchange(A, i, largest)
        max_heapify(A, size -1, largest)

def exchange(A, i, largest):
    """ 
    Swaps items in A.
    """
    temp = A[i]
    A[i] = A[largest]
    A[largest] = temp

def parent(i):
    """
    Returns the index of the parent of the node at index i.
    """
    return i // 2

def left(i):
    """
    Returns the index of the left child of the node at index i.
    """
    return 2*i

def right(i):
    """
    Returns the index of the right child of the node at index i.
    """
    return 2*i + 1

if __name__ == "__main__":
    # Example usage
    A = [2,7,26,25,19,17,1,90,3,36]
    heap_sort(A)
    print(A)
