from array_sequence import ArraySequence
from dynamic_array import DynamicArraySequence
import matplotlib.pyplot as plt
import seaborn as sns
import time
import numpy as np

sns.set_theme()

n_list = range(1,5000,1)

# Analyse insert_last()

array1 = ArraySequence()
dynamic_array1 = DynamicArraySequence()
list1 = []

array_times_insert_last = []
dynamic_array_times_insert_last = []
list_times_insert_last = []

for n in n_list:

    start = time.perf_counter()
    array1.insert_last(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    array_times_insert_last.append(elapsed_time)

    start = time.perf_counter()
    dynamic_array1.insert_last(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    dynamic_array_times_insert_last.append(elapsed_time)

    start = time.perf_counter()
    list1.append(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    list_times_insert_last.append(elapsed_time)

cumulative_average_array_last = np.cumsum(array_times_insert_last)/np.array(n_list)
cumulative_average_dynamic_array_last = np.cumsum(dynamic_array_times_insert_last)/np.array(n_list)
cumulative_average_lists_last = np.cumsum(list_times_insert_last)/np.array(n_list)

# Analyse insert_first()

array1 = ArraySequence()
dynamic_array1 = DynamicArraySequence()
list1 = []

array_times_insert_first = []
dynamic_array_times_insert_first = []
list_times_insert_first = []

for n in n_list:

    start = time.perf_counter()
    array1.insert_first(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    array_times_insert_first.append(elapsed_time)

    start = time.perf_counter()
    dynamic_array1.insert_first(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    dynamic_array_times_insert_first.append(elapsed_time)

    start = time.perf_counter()
    list1.insert(0,1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    list_times_insert_first.append(elapsed_time)

cumulative_average_array_first = np.cumsum(array_times_insert_first)/np.array(n_list)
cumulative_average_dynamic_array_first = np.cumsum(dynamic_array_times_insert_first)/np.array(n_list)
cumulative_average_lists_first = np.cumsum(list_times_insert_first)/np.array(n_list)


#plt.plot(n_list, cumulative_average_array_last, label="Array insert_last()", marker="x")
#plt.plot(n_list, cumulative_average_dynamic_array_last, label="Dynamic Array insert_last()", marker=".")
plt.plot(n_list, cumulative_average_lists_last, label="Python List insert_last()", marker="o")

#plt.plot(n_list, cumulative_average_array_first, label="Array insert_first()", marker="x")
#plt.plot(n_list, cumulative_average_dynamic_array_first, label="Dynamic Array insert_first()", marker=".")
plt.plot(n_list, cumulative_average_lists_first, label="Python List insert_first()", marker="o")


plt.title("Analysis of insert_last() and insert_first()")
plt.legend()
plt.xlabel("n")
plt.ylabel("Average Time (s)")
plt.show()
