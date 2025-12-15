from array_sequence import ArraySequence
from dynamic_array import DynamicArraySequence
import matplotlib.pyplot as plt
import seaborn as sns
import time
import numpy as np

sns.set_theme()

N = 50

n_list = np.arange(1,N,1)
array1 = ArraySequence()
dynamic_array1 = DynamicArraySequence()
list1 = []

array_times = []
dynamic_array_times = []
list_times = []

for n in n_list:
    start = time.perf_counter()
    array1.insert_last(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    array_times.append(elapsed_time)

    start = time.perf_counter()
    dynamic_array1.insert_last(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    dynamic_array_times.append(elapsed_time)

    start = time.perf_counter()
    list1.append(1)
    finish = time.perf_counter()
    elapsed_time = finish - start
    list_times.append(elapsed_time)
    


plt.bar(n_list-0.3, array_times, label="Array", width=0.4)
plt.bar(n_list, dynamic_array_times, label="Dynamic Array", width=0.4)
#plt.bar(n_list+0.3, list_times, label="Python List", width=0.4)


plt.title("Analysis of insert_last()")
plt.legend()
plt.xlabel("n")
plt.ylabel("Time (s)")
plt.show()
