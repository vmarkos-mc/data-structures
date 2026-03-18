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
    n = len(ns)
    if n == 0:
        return [] # Returns a **new** empty list
    if n == 1:
        return [ns[0]] # Again, returns a copy of the input list
    middle = n // 2 # BEWARE: Integer division!
    left = ns[:middle] # Up to `middle - 1`
    right = ns[middle:] # From `middle`
    return __merge(merge_sort(left), merge_sort(right))


def __merge(a, b):
    """Implements order respecting merging of `a` and `b`"""
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]: # or `a[i] <= b[j]`, which also preserves initial ordering.
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a): # If `a` was exhausted first
        c += b[j:] # then just copy the rest of `b`
    else: # equivalent to `elif j == len(b)`
        c += a[i:] # otherwise, just copy the rest of `a`
    return c


def debug():
    a = [1, 3, 6, 8, 9]
    b = [0, 1, 2, 3, 4, 8]
    c = __merge(a, b)
    print(c)


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
    # debug()