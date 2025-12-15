from matplotlib import pyplot as plt

def plot_complexity(bubble_fn = "bubbleResults.txt", merge_fn = "mergeResults.txt"):
    with open(bubble_fn, "r") as f:
        bubble_res = [int(x) for x in f.read().split(",")]
    with open(merge_fn, "r") as f:
        merge_res = [int(x) for x in f.read().split(",")]
    n = len(bubble_res)
    x = [i for i in range(1, n + 1)]
    plt.plot(x, bubble_res, label = "Bubble sort")
    plt.plot(x, merge_res, label = "Merge sort")
    plt.xlabel("Array size", fontsize = 18)
    plt.ylabel("Time (ns)", fontsize = 18)
    plt.title("Time complexity of Bubble- and Merge- sort", fontsize = 24)
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    plot_complexity()