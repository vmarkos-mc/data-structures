from doubly_linked_list_full import DoublyLinkedList
import random

# we will reuse our linked list class and attach a key value pair as the data.
# we could just create a new doubly linked-list class that had nodes that were just held the key value pair
# this would probably be more appropriate, but I wanted to reuse our existing class
class KeyValuePair:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        # we could choose to delete the item, instead we flag it as deleted
        # this does cost space, but saves time. Which would be better and under what circumstances
        self.deleted = False

    def __str__(self):
        return f"Key:{self.key}, Value:{self.value}, Deleted:{self.deleted}"

class HashTable:
    # initialise
    def __init__(self, verbose=False):
        # create a list 
        self.capacity = 10
        self.buckets = [None]*self.capacity
        self._size = 0
        self.verbose = verbose

    def __str__(self):
        if self.verbose:
            return self._print_internal()
        desc = "{"
        for bucket in self.buckets:
            if bucket != None:
                node = bucket.head
                while node != None:
                    desc += f"{node.data.key}: {node.data.value}, "
                    node = node.next
        desc = desc[:-2] + "}"
        return desc 
    
    def _print_internal(self):
        desc = ""
        for i, bucket in enumerate(self.buckets):
            desc += f"\n | {i} | -> "
            if bucket != None:
                desc += f"[size={bucket.size()}]<"
                #desc += str(bucket)
            else:
                desc += "Empty"
            desc += ">"
        return desc 

    def create(self, X):
        # implement last
        pass

    def get(self, k):
        # call hashing function and return index i
        # get linked list from list at index i
        # find k in linked list and return value
        kv_pair = self._find(k)
        if kv_pair != None:
            if kv_pair.deleted:
                raise Exception("Key does not exist in Hash Table")
            if self.verbose: print(f"Found key:value - {kv_pair.key}:{kv_pair.value}") # print out verbose for debugging
            return kv_pair.value
        else:
            raise Exception("Key does not exist in Hash Table")

    def put(self, k,v):
        # call hashing function and return index i
        # get linked list from list at index i
        # if k in linked_list overwrite value
        # else insert (k,v) pair at front of linked list
        hash_k = self._hash_function(k)

        # bucket empty, thus key not in hash table
        if self.buckets[hash_k] == None:
            self.buckets[hash_k] = DoublyLinkedList()
        
        kv_pair = self._find(k)
        if kv_pair != None:
            # key already in hash table, overwrite value
            kv_pair.value = v
            kv_pair.deleted = False
        else:
            # insert at front of linked list
            self.buckets[hash_k].insert_first(KeyValuePair(k,v))
            self._size += 1
        if self.verbose: print(f"Added key:value - {k}:{v}") # print out verbose for debugging
        
    def remove(self, k):
        # call hashing function and return index i
        # get linked list from list at index i
        # remove (k,v) pair from linked list
        kv_pair = self._find(k)
        if kv_pair != None:
            if kv_pair.deleted:
                raise Exception("Key does not exist in Hash Table")
    
            kv_pair.deleted = True
            self._size -= 1
            if self.verbose: print(f"Deleted key:value - {kv_pair.key}:{kv_pair.value}") # print out verbose for debugging
        else:
            raise Exception("Key does not exist in Hash Table")
        
    def size(self):
        return self._size

    def _find(self, k):
        """ return KeyValuePair if found else None"""
        hash_k = self._hash_function(k)
        bucket = self.buckets[hash_k]
        if bucket is None:
            return None
        current_node = bucket.head
        while current_node != None:
            if current_node.data.key == k:
                return current_node.data
            current_node = current_node.next

        return None

    def _hash_function(self, k):
        hash_total = 0
        k_str = str(k)
        for char in k_str:
            hash_total += ord(char)**len(k_str)

        # return the modulus (capacity) - clock arithmetic, keeps number between 0 and capacity - 1
        return hash_total % self.capacity


if __name__ == "__main__":
    h = HashTable(verbose=True)
    print(h)
    h.put(12, "Sam")
    h.put(22, "Joe")
    h.put(24, "Em")
    h.put(123, "Matt")
    print(h)
    print(h.get(12))
    print(h.get(22))
    print(h.get(123))
    h.put(123, "John")
    print(h)
    print(h.get(123))
    print(f"The size of the hash table is {h.size()}")
    h.remove(123)
    print(h)
    print(f"The size of the hash table is {h.size()}")
    h.put(123, "John1")
    print(h)
    print(f"The size of the hash table is {h.size()}")
    print(h.get(123))
    print(h)

    h1 = HashTable(verbose=True)

    for x in [random.randint(1,10000) for _ in range(100)]:
        h1.put(x,x)

    print(h1)