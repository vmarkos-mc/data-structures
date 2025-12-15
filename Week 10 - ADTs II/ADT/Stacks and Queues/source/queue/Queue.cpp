#include <stdexcept> // Used to throw some exceptions.
#include <iostream> // Used to print stuff out.

using namespace std;

template <typename T>
class Queue {
    private:
        int _size;
        int _head; // Where we pop elements from
        int _count; // How many elements we have
        T* _queue;

    public:
        Queue(int size) {
            _size = size;
            _head = 0;
            _count = 0;
            _queue = new T[_size];
        }

        ~Queue() {
            delete[] _queue;
        }

        void enqueue(T item) {
            if (_count == _size) {
                throw out_of_range("Queue Overflow!");
            }
            _queue[(_head + _count) % _size] = item;
            _count++;
            cout << "Enqueued: " << item << ". Head: " << _head << ". Tail: " << (_head + _count) % _size << endl;
        }

        T dequeue() {
            if (_count == 0) {
                throw out_of_range("Queue Underflow!");
            }
            T item = _queue[_head];
            _head = (_head + 1) % _size;
            _count--;
            cout << "Dequeued: " << item << ". Head: " << _head << ". Tail: " << (_head + _count) % _size << endl;
            return item;
        }
};

int main() {
    Queue<int> q = Queue<int>(4);
    q.enqueue(3);
    q.enqueue(2);
    q.dequeue();
    q.enqueue(6);
    q.dequeue();
    return 0;
}