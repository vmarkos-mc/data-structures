from array_sequence import ArraySequence
from dynamic_array import DynamicArraySequence
import matplotlib.pyplot as plt
import seaborn as sns
import time
import numpy as np

sns.set_theme()

N = 5000

n_list = np.arange(1,N,1)

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
    


#plt.bar(n_list-0.3, array_times_insert_first, label="Array insert_first()", width=0.4)
#plt.bar(n_list-0.3, array_times_insert_last, label="Array insert_last()", width=0.4)

#plt.bar(n_list -0.2, dynamic_array_times_insert_first, label="Dynamic Array insert_first()", width=0.4)
#plt.bar(n_list + 0.2, dynamic_array_times_insert_last, label="Dynamic Array insert_last()", width=0.4)
sns.set_context(rc = {'patch.linewidth': 0.0})
plt.bar(n_list[::10] - 0.2, list_times_insert_first[::10], label="Python List insert_first()", width=5)
plt.bar(n_list[::10] + 0.2, list_times_insert_last[::10], label="Python List insert_last()", width=5)

plt.title("Analysis of insert_first and insert_last()")
plt.legend()
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.show()
