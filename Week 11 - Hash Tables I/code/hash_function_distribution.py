import random
import matplotlib.pyplot as plt

# Define hash function that maps all keys to the value 1
def hash_func1(key):
    return 1 

# Define hash function that maps keys to a the range 0-999
def hash_func3(key):
    return key % 100

# Define hash function that maps keys to a a more uniform distribution of hash values in the range 0-999
def hash_func2(key):
    hash_value = key**2 % 100
    return hash_value % 100

def python_hash(key):
    return hash(key)


# Generate random keys and compute their hash values using all three functions
keys = [random.randint(0, 9999) for _ in range(1000)]
hashes1 = [hash_func1(key) for key in keys]
hashes2 = [hash_func2(key) for key in keys]
hashes3 = [hash_func3(key) for key in keys]
hashes4 = [python_hash(key) for key in keys]

# Plot the distribution of hash values for all three functions side-by-side
fig, axs = plt.subplots(2, 2, figsize=(15, 5))
axs[0][0].hist(hashes1, bins=1)
axs[0][0].set_xticks(range(0,101,20))
axs[0][0].set_yticks(range(0,1001,200))
axs[0][0].set_title("Hash Function 1 (Poor)")
axs[0][0].set_xlabel("Hash Value")
axs[0][0].set_ylabel("Frequency")
axs[0][1].hist(hashes2, bins=100)
axs[0][1].set_xticks(range(0,101,20))
axs[0][1].set_yticks(range(0,101,20))
axs[0][1].set_title("Hash Function 2 (OK)")
axs[0][1].set_xlabel("Hash Value")
axs[0][1].set_ylabel("Frequency")
axs[1][0].hist(hashes3, bins=100)
axs[1][0].set_xticks(range(0,101,20))
axs[1][0].set_yticks(range(0,101,20))
axs[1][0].set_title("Hash Function 3 (Better)")
axs[1][0].set_xlabel("Hash Value")
axs[1][0].set_ylabel("Frequency")
axs[1][1].hist(hashes4, bins=100)
axs[1][1].set_yticks(range(0,101,20))
axs[1][1].set_title("Python Hash Function")
axs[1][1].set_xlabel("Hash Value")
axs[1][1].set_ylabel("Frequency")
plt.subplots_adjust(wspace=0.4, bottom=0.2)
plt.subplots_adjust(hspace=0.6, bottom=0.2)
#plt.title("Comparison of hashing numbers 0-9999")
plt.savefig("hash_functions_compared.png")
plt.show()
