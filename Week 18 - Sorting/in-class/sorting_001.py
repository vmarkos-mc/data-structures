# in-class/sorting_001.py

def bubble_sort(ns) -> list:
    """Implements bubble sort, returning a new list"""
    ...


def merge_sort(ns) -> list:
    """Implements merge sort, returning a new list"""
    ...


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