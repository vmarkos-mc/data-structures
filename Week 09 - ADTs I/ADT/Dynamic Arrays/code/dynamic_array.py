# Adapted from https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020

# This could be optimised more, but it demonstrates how you can implement insert and shift using a reize

class DynamicArraySequence:
    """ This is to demonstrate how an array might look in other languages
        Because Python supports lists we are actually not gaining anything here
        We have also implemented insert and delete"""
    def __init__(self):
        self.A = None 
        self._no_items = 0
        self._upper = 0
        self._r = 2

    def __str__(self):
        desc = "Items in array - ["
        for x in self.A:
            desc += f"{x} "
        desc += f"] \nno items = {self._no_items} \nsize of array = {self._upper}\n"
        return desc

    def create(self, X):
        for x in X:
            self.insert_last(x)
            print(self.__str__())
        
    def _set_lower_upper(self, upper):
        self._upper = upper
        self._lower = int((1/(self._r+1))*self._upper)

    def size(self): return self._no_items

    def get_at(self, i): return self.A[i]

    def set_at(self, i, x): self.A[i] = x

    def _forward_left_copy(self, start, end, B):
        """ copy items to the left by 1 from self.A into B"""
        for k in range(start, end):                             # copy items from A to B using a forward left copy
            B[k] = self.A[k + 1]

    def _backward_right_copy(self, end, start, B):
        """ copy items to the right by 1 from self.A into B"""
        for k in range(end, start, -1):                         # copy items from A to B using a backward right copy
            B[k] = self.A[k-1]

    def _copy(self, start, end, B):
        """ copy items to from self.A into B"""
        for k in range(start, end):                             # copy items from A to B by the same index
            B[k] = self.A[k]

    def _increase_size(self):
        if self._no_items + 1 > self._upper:                    # check if array should be resized
            new_size = int(max(self._upper * self._r, 1))       # calculate new size
            self._resize(new_size)                              # perform resize

    def _decrease_size(self):
        if self._no_items <= self._lower:                       # check if array should be resized
            new_size = int(max(self._upper * (1/self._r), 1))   # calculate new size
            self._resize(new_size)                              # perform resize

    def _resize(self, new_size):
        B = [None] * new_size                                   # create a new array of new_size
        self._copy(0, self._no_items, B)                        # copy across every current item to B
        self.A = B                                              # overwrite self.A with newly resize copy B
        self._set_lower_upper(new_size)                     # set the upper to new_size and lower to threshold

    def insert(self, i, x):
        self.insert_last(None)                                  # insert a blank item as the last item, this will cause a resize if needed
        self._backward_right_copy(self._no_items-1, i, self.A)  # do a backward right copy for items after insertion
        self.A[i] = x                                           # perform insert at index i
  
    def delete(self, i):
        x = self.A[i]                                           # copy item to be removed to x
        self._forward_left_copy(i, self._no_items-1, self.A)    # do a forward left copy for items after deletion
        self.delete_last()                                      # delete last item
        return x                                                # return the removed item. like pop() in Python

    def insert_last(self, x):
        self._increase_size()                                   # check for and perform resize if needed
        self.A[self._no_items] = x                              # insert item at the end of items
        self._no_items += 1                                     # increase no items by 1

    def delete_last(self):
        # check there is something in the array to delete
        if self._no_items > 0:
            self.A[self._no_items-1] = None                     # set last item to None
            self._no_items -= 1                                 # decrease no items by 1
            self._decrease_size()                               # check for resize and perform resize if needed

    def insert_first(self, x):
        self.insert(0,x)
    
    def delete_first(self):
        self.delete(0)

    
if __name__ == "__main__":
    A = DynamicArraySequence()
    A.create([1,2,3,4])
    print(A) # should print 1 2 3 4
    A.insert(1,99)
    print(A) # should print 1 99 2 3 4
    A.insert(4,999)
    print(A) # should print 1 99 2 3 999 4
    A.delete(2)
    print(A) # should print 1 99 3 999 4
    A.delete_last()
    print(A) # should print 1 99 3 999
    A.delete_last()
    print(A) # should print 1 99 3
    A.delete_last()
    print(A) # should print 1 99 
    x = A.delete_last()
    print(A) # should print 1 
    x = A.delete_last()
    print(A) # should print 1 
    x = A.delete_last()
    print(A) # should print 1 
    
    print("---------B---------")
    B = DynamicArraySequence()
    B.create([1,2,3,4])
    print(B)
    for i in range(10):
        B.insert_last(i)
    print(B)

    for i in range(12):
        B.delete_last()

    print(B)
    