class ArraySequence:
    """ This is to demonstrate how an array might look in other languages
        Because Python supports lists we are actually not gaining anything here
        We have also implemented insert and delete"""
    def __init__(self):
        self.A = None
        self._size = 0

    def __str__(self):
        desc = ""
        for x in self.A:
            desc += f"{x} "
        desc += f"- size = {self._size}"
        return desc

    def create(self, X):
        self.A = [a for a in X] # Imagine this builds a static array in memory
        for x in self.A:
            self._size += 1

    def size(self): return self._size

    def get_at(self, i): return self.A[i]

    def set_at(self, i, x): self.A[i] = x

    def _copy(self, start, end, B):
        """ copy items from self.A into B"""
        for k in range(start, end):
            B[k] = self.A[k]

    def _forward_right_copy(self, start, end, B):
        """ copy items to the right by 1 from self.A into B"""
        for k in range(start, end):
            B[k] = self.A[k - 1]

    def _forward_left_copy(self, start, end, B):
        """ copy items to the left by 1 from self.A into B"""
        for k in range(start, end):
            B[k] = self.A[k + 1]
            
    def insert(self, i, x):
        n = self._size
        B = [None] * (n+1)  # create a new array of size n
        
        self._copy(0, i, B)
        self._forward_right_copy(i+1, n+1, B)
        B[i] = x

        self.A = B
        self._size += 1

    def delete(self, i):
        n = self._size
        B = [None] * (n-1)
        
        self._copy(0, i, B)
        self._forward_left_copy(i, n-1, B)

        self.A = B
        self._size -= 1

    def insert_first(self, x):
        self.insert(0,x)

    def insert_last(self, x):
        self.insert(self._size, x)

    def delete_first(self):
        self.delete(0)

    def delete_last(self):
        self.delete(self._size - 1)

if __name__ == "__main__":
    A = ArraySequence()
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