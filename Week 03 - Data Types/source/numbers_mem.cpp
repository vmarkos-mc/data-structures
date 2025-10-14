// source/numbers_mem.cpp
#include <iostream> // Allows us to print stuff
using namespace std; // A spell that saves us from some typing

int main() { // Another spell...
    int x = 42; // Just an integer...
    cout << "x: " << x << " at: " << &x << endl; // Print some stuff
    int* ptrx = &x; // Store the memory location of x.
    float* ptry = (float*) ptrx; // Store the same memory location (casting to float)
    cout << "x: " << *ptry << " at: " << &x << endl; // What will this print?
    return 0; // One last spell...
}

/*
Some notes:
    * In C/C++, &x, where x is some variable yields the memory location 
      where x is kept.
    * In C/C++ `<type>* <var_name>` declares a pointer, i.e., an integer
      number that points to the memory location of a variable. That is,
      writing int* ptrx = &x, we store the address of x, given by &x, to
      a pointer named ptrx.
    * We can change the type of a variable in C/C++ by inserting in 
      parentheses the desired new type. So, in line 9 we actually just 
      change the pointer from one pointing to integers to one pointing
      to floats. So the computer now thinks there is a 
    * Using the asterisk we can also retrieve the value kept in a 
      certain memory location. So, *ptrx actually gives us back the 
      numerical value kept at location ptrx.
*/