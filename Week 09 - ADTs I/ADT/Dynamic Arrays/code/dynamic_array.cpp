#include <iostream>
#include <stdexcept>
#include <sstream>

class DynamicIntArray {
private:
    int* arr;            // Pointer to the dynamic array
    int size;            // Current number of elements in the array
    int capacity;        // Current capacity of the array
    int initialCapacity = 1;
    double GrowthFactor = 2.0;

public:
    // Constructor with default capacity and growth factor
    DynamicIntArray() {
        // Allocate a new array with the specified initial capacity
        arr = new int[initialCapacity];
    
        // Set the initial size to 0, as the array is empty
        size = 0;
    
        // Set the initial capacity to the specified value
        capacity = initialCapacity;
    }

    // Destructor to free allocated memory
    ~DynamicIntArray() {
        delete[] arr;
    }

    // Get the element at the specified index
    int get(int index) const {
        // Check if the index is within bounds
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        return arr[index];
    }
    
    int getCapacity(){
        return capacity;
    }
    
    int getSize(){
        return size;
    }

    // Set the element at the specified index to the given item
    void set(int index, int item) {
        // Check if the index is within bounds
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }
        arr[index] = item;
    }

    // Insert the given item at the specified index
    void insert(int index, int item) {
        // Check if the index is within bounds
        if (index < 0 || index > size) {
            throw std::out_of_range("Index out of bounds");
        }

        // If the array is full, resize it
        if (size == capacity) {
            resize();
        }

        // Shift elements to make space for the new item
        for (int i = size; i > index; --i) {
            arr[i] = arr[i - 1];
        }

        // Insert the new item at the specified index
        arr[index] = item;

        // Increment the size
        ++size;
    }

    // Delete the element at the specified index
    void erase(int index) {
        // Check if the index is within bounds
        if (index < 0 || index >= size) {
            throw std::out_of_range("Index out of bounds");
        }

        // Shift elements to fill the gap created by deleting the item
        for (int i = index; i < size - 1; ++i) {
            arr[i] = arr[i + 1];
        }

        // Decrement the size
        --size;
    }
    
    // Convert the contents of the array to a string
    std::string toString() const {
        std::stringstream ss;
        ss << "[";
        for (int i = 0; i < size; ++i) {
            ss << arr[i];
            if (i < size - 1) {
                ss << ", ";
            }
        }
        ss << "]";
        return ss.str();
    }

    // Add an item to the end of the array
    void push_back(int item) {
        // If the array is full, resize it
        if (size == capacity) {
            resize();
        }

        // Add the item to the end of the array
        arr[size] = item;

        // Increment the size
        ++size;
    }

    // Remove the last item from the array
    void pop_back() {
        // Check if the array is not empty
        if (size > 0) {
            // Decrement the size to effectively "remove" the last item
            --size;
        } else {
            throw std::out_of_range("Array is empty");
        }
    }

private:
    // Helper function to resize the array
    void resize() {
        // Calculate the new capacity based on the growth factor
        int newCapacity = static_cast<int>(capacity * GrowthFactor);

        // Allocate a new array with the updated capacity
        int* newArr = new int[newCapacity];

        // Copy elements from the old array to the new array
        for (int i = 0; i < size; ++i) {
            newArr[i] = arr[i];
        }

        // Free the memory occupied by the old array
        delete[] arr;

        // Update the pointer and capacity
        arr = newArr;
        capacity = newCapacity;
    }
};

int main() {
    // Example usage
    DynamicIntArray myArray;

    // Adding elements to the array
    myArray.push_back(10);
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;
    myArray.push_back(20);
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;
    myArray.push_back(30);
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;
    myArray.push_back(40);
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;
    myArray.push_back(50);
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;

    // Accessing elements
    std::cout << "Element at index 1: " << myArray.get(1) << std::endl;

    // Modifying elements
    myArray.set(1, 25);
    std::cout << "Modified element at index 1: " << myArray.get(1) << std::endl;

    // Inserting an element
    myArray.insert(1, 15);
    std::cout << "After insertion at index 1: " << myArray.get(1) << std::endl;

    // Deleting an element
    myArray.erase(2);
    std::cout << "After deletion at index 2: " << myArray.get(2) << std::endl;

    // Removing the last element
    myArray.pop_back();
    std::cout << "After pop_back(): Size is now " << myArray.getSize() << std::endl;
    std::cout << "Size: " << myArray.getSize() << " Capacity: " << myArray.getCapacity() << " Contents: " << myArray.toString() << std::endl;

    return 0;
}
