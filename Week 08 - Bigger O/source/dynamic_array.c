// source/dynamic_array.c
/*
This is a sample file that defines and presents a simple use
of a dynamically allocated array of integers.

All relevant functions include some prints, mostly for debugging
and teaching purposes. Typically, you shouldn't use such prints 
in a production level implementation.
*/

#include <stdlib.h> // For several stuff, like size_t
#include <stdio.h> // Used to print stuff

typedef struct dynamicArray {
    int* array; // Pointer pointing to array start
    // size_t is just an unsigned integer (plus some quirks)
    size_t used; // `used` will be used to denote the used part of the array
    size_t size; // `size` will be used to denote the total available size of the array
} dynamicArray;

void createArray(dynamicArray* arr, size_t initSize) {
    if (initSize < 1) { // Just to make sure the user does not go goofy...
        initSize = 10;
    }
    arr->array = malloc(initSize * sizeof(int)); // Allocate required memory for the array
    arr->used = 0; // No bytes have been used yet, just allocated
    arr->size = initSize; // However, the size of the array, even if unused, is non-trivial
    printf("Initialised array of size: %zu\n", initSize); // %zu is C99 and used to print long unsigned numbers
}

void insertArray(dynamicArray* arr, int e) {
    if (arr->used == arr->size) { // In case the array gets full (used part == size)...
        arr->size = arr->size + 8; // Increase the size available for the array
        arr->array = realloc(arr->array, arr->size * sizeof(int)); // Reallocate memory (expand)
        printf("Array full, expanding to %zu bytes.\n", arr->size);
    }
    arr->array[arr->used] = e; // Add the new element to the array
    arr->used++; // Increment the used part by one...
    printf("Inserted element: %d; used: %zu, size: %zu.\n", e, arr->used, arr->size);
}

void freeArray(dynamicArray* arr) {
    free(arr->array); // First, we deallocate the actual array pointer where all memory has been allocated to
    arr->array = NULL; // Then NULLify the pointer to make sure it doe not point to deallocated memory (!)
    printf("Deallocated array, bytes used %zu, bytes freed: %zu\n", arr->used, arr->size);
    arr->used = 0; // Just to make sure all things are semantically correct
    arr->size = 0; // Just to make sure all things are semantically correct
}

void printArray(dynamicArray* arr) {
    printf("[ ");
    for (int i = 0; i < arr->used; i++) {
        printf("%d ", *(arr->array + i));
    }
    printf("]\n");
}

int main() {
    dynamicArray a;
    createArray(&a, 4);
    for (int i = 0; i < 25; i++) {
        insertArray(&a, i);
    }
    printArray(&a);
    freeArray(&a);
    return 0;
}

/*
Some general comments:
1. When meddling around with pointers, it is important to perform sufficient bound checks.
2. We did not do this here, mostly to make our code more readable.
3. However, in a complete solution, we should check the outputs of malloc and realloc for NULLs.
4. However^2, many times we intentionally avoid bound checking since it increases execution time significantly.
5. In any case, bound checking is a decision you have to make consciously and not by accident!
*/