#include <iostream>
#include <stdexcept>
#include <string>

using namespace std;

template <typename T>
class DynamicArray {
    private:
        T* _arr;
        int _size;
        int _GROW_FACTOR;
        int _SHRINK_FACTOR;
        int _filled_count;
        
        void _grow() {
            _size *= _GROW_FACTOR;
            T* _grown_arr = new T[_size];
            for (int i = 0; i < _size; i++) {
                _grown_arr[i] = _arr[i];
            }
            delete[] _arr;
            _arr = _grown_arr;
        }
        
        void _shrink() {
            _size *= _SHRINK_FACTOR;
            T* _shrinked_arr = new T[_size];
            for (int i = 0; i < _size; i++) {
                _shrinked_arr[i] = _arr[i];
            }
            delete[] _arr;
            _arr = _shrinked_arr;
        }
        
        void _push_right(int index) {
            for (int i = _size - 1; i >= index; i--) {
                _arr[i + 1] = _arr[i];
            }
        }
        
    public:
        DynamicArray(int size, int GROW_FACTOR = 2, int SHRINK_FACTOR = 0.33) {
            _size = size;
            _arr = new T[_size];
            _filled_count = 0;
            _GROW_FACTOR = GROW_FACTOR;
            _SHRINK_FACTOR = SHRINK_FACTOR;
        }
        
        ~DynamicArray() {
            delete[] _arr;
        }
        
        const T& operator[] (int idx) { // FIXME What else should be done here?
            return _arr[idx];
        }
        
        string to_string() {
            string out_str= "";
            for (int i = 0; i < _size; i++) {
                out_str += _arr[i];
                if (i < _size - 1) {
                    out_str += ", ";
                }
            }
            return out_str;
        }
        
        void insert(int index, T item) {
            if (index > _size - 1 || index < 0) {
                throw out_of_range("Index out of range!"); // FIXME Is this correct?
            }
            if (_filled_count > _size) {
                _grow();
            }
            _push_right(index);
            _arr[index] = item;
            cout << "Inserted: " << item << " at " << index << ". Array: " << to_string() << endl;
        }
};

int main() {
    DynamicArray<int> d = DynamicArray<int>(10);
    d.insert(0, 10);
}