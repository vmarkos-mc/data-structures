# in-class/heap_main.py

from MaxHeap import MaxHeap

def main():
    heap = MaxHeap()
    heap.add(3)
    heap.add(2)
    heap.add(5)
    heap.add(9)
    heap.add(8)
    print(f"Heap has length: {len(heap)}")
    while heap: # i.e., while our heap is not empty
        print(heap.pop())


if __name__ == "__main__":
    main()