# in-class/sorting_001.py

def bubble_sort(ns, key = lambda x, y: x >= y) -> list:
    """Implements bubble sort, returning a new list"""
    sorted_ns = [x for x in ns] # To make sure we do not mutate `ns`
    swapped = True # Just to make sure we enter the while loop
    n = len(sorted_ns)
    while swapped and n > 1:
        swapped = False
        for i in range(1, n):
            if not key(sorted_ns[i], sorted_ns[i - 1]):
                sorted_ns[i - 1], sorted_ns[i] = sorted_ns[i], sorted_ns[i - 1]
                swapped = True
                # temp = sorted_ns[i]
                # sorted_ns[i] = sorted_ns[i - 1]
                # sorted_ns[i - 1] = temp
        n -= 1
    return sorted_ns


def merge_sort(ns) -> list:
    """Implements merge sort, returning a new list"""
    return ns


def list_to_str(ls) -> str:
    return f"[{', '.join(str(x) for x in ls)}]"

def main():
    a = [7, 3, 2, 1, 9, 0, 3, 1, 6]
    b = bubble_sort(a)
    c = merge_sort(a)
    print(f"a: {list_to_str(a)}")
    print(f"b: {list_to_str(b)}")
    print(f"c: {list_to_str(c)}")

if __name__ == "__main__":
    main()