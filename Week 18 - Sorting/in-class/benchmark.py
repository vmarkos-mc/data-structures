# in-class/benchmark.py

import random
import time
from matplotlib import pyplot as plt # Used for plotting
from sorting_001 import bubble_sort, merge_sort


def test(sorting_fn, N=100, m=100):
    """Tests the input sorting function `m` times on inputs of size `range(1,N)`"""
    timings = []
    for _ in range(1, N): # Run for different values up to `N`
        timings.append([])
        for _ in range(m):
            # Generate a list of `N` random integers in range 0,...,N-1
            ns = random.choices(range(N), k=N)
            start = time.time()
            sorting_fn(ns)
            end = time.time()
            exec_time = end - start
            timings[-1].append(exec_time)
    return timings


def avg(ns):
    if len(ns) == 0:
        raise ValueError("Empty list!")
    return sum(ns) / len(ns)


def plot(bubble_avg_timings, merge_avg_timings):
    plt.plot(bubble_avg_timings, label="bubble sort")
    plt.plot(merge_avg_timings, label="merge sort")
    plt.legend()
    plt.show()


def main():
    bubble_timings = test(bubble_sort, N=200, m=500)
    merge_timings = test(merge_sort, N=200, m=500)
    bubble_avg_timings = [avg(row) for row in bubble_timings]
    merge_avg_timings = [avg(row) for row in merge_timings]
    plot(bubble_avg_timings, merge_avg_timings)


if __name__ == "__main__":
    main()