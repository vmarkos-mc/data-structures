// Queue.c
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h> // `<>` are used for system header files
#include "Queue.h" // `""` are used for local header files

Queue* queue_create(int capacity) {
    // malloc() always returns a void*, so we need to cast
    // it to whatever pointer we need to.
    Queue* queue = (Queue*) malloc(sizeof(Queue));
    queue->capacity = capacity;
    queue->first = -1; // -1 indicating nothing in queue
    queue->count = 0;
    queue->queue = (int*) malloc(sizeof(int) * capacity);
    return queue;
}

void queue_destroy(Queue** queue_p) {
    if (queue_p == NULL || *queue_p == NULL)
        return;
    Queue* queue = *queue_p; // Just to make things simpler
    for (int i = 0; i < queue->capacity; i++)
        *(queue->queue + i) = 0; // Make all queue elements == 0
    free(queue->queue); // This frees up any allocated memory
    queue->queue = NULL; // Make sure we forget were this array was
    // Clean up any integers
    queue->capacity = 0;
    queue->count = 0;
    queue->first = 0;
    // Free the que struct itself
    free(queue);
    // Make the Queue pointer null
    *queue_p = NULL;
}

bool queue_insert(Queue* queue, int item) {
    if (queue_is_full(queue)) return false;
    // queue->count++;
    int i = queue->first + (++queue->count);
    *(queue->queue + i) = item;
    return true;
}

bool queue_dequeue(Queue* queue, int* item) {
    if (queue_is_empty(queue)) return false;
    queue->first = (queue->first + 1) % queue->capacity;
    *item = *(queue->queue + (queue->first));
    queue->count--;
    return true;
}

bool queue_is_full(Queue* queue) {
    return queue->count == queue->capacity;
}

bool queue_is_empty(Queue* queue) {
    return queue->count == 0;
}