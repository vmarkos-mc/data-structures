#include <stdexcept> // Used to throw some exceptions.
#include <iostream> // Used to print stuff out.

using namespace std;

template <typename T>
class Stack {
    private:
        int _size;
        int _stack_ptr;
        T* _stack;

    public:
        Stack(int size) {
            _size = size;
            _stack_ptr = -1;
            _stack = new T[_size];
        }

        ~Stack() {
            delete[] _stack;
        }

        T pop() {
            if (_stack_ptr == -1) {
                throw out_of_range("Stack Underflow!");
            }
            _stack_ptr--;
            cout << "Popped " << _stack[_stack_ptr + 1] << ". stack pointer: " << _stack_ptr << endl;
            return _stack[_stack_ptr + 1];
        }

        void push(T item) {
            if (_stack_ptr == _size - 1) {
                throw out_of_range("Stack Overflow!");
            }
            _stack_ptr++;
            _stack[_stack_ptr] = item;
            cout << "Pushed " << item << ". stack pointer: " << _stack_ptr << endl;
        }
};

int main() {
    Stack<int> s = Stack<int>(3);
    s.push(5);
    s.push(6);
    s.push(3);
    s.pop();
    s.pop();
    s.push(4);
    s.pop();
    s.pop();
    return 0;
}