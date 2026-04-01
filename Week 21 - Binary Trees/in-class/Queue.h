#ifndef QUEUE_H
#define QUEUE_H

/*
#define is a pre-processor command (macro) that defines a constant, effectively a 
guard that ensures we do not import the same header file multiple times.
*/ 

// Queue.h
/*
Typically, in C development, we split logic into two separate components:

    * source files, which include implementations of things we want to implement, and;
    * header files, which include declarations of things we want to implement.

Also, it is customary to denote source file with a `.c` file extension and header files with 
a `.h` file extension.
*/

#include <stdbool.h>

typedef struct Queue {
    int capacity; // Queue capacity
    int first; // Index of first element (next to dequeue)
    int count; // Number of items already in queue
    int* queue; // Integer pointer, i.e., array of integers
} Queue;

Queue* queue_create(int);
void queue_destroy(Queue**);
bool queue_insert(Queue*, int);
bool queue_dequeue(Queue*, int*);

bool queue_is_full(Queue*);
bool queue_is_empty(Queue*);

#endif