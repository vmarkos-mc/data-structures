#include <iostream>

int main() {
    int x = 3;
    int y = 2;

    int* p = &x;     // Declare a pointer to x
    int* q = &y;     // Declare a pointer to y

    std::cout << "Value of x: " << x << "\n";
    std::cout << "Value of x through pointer p: " << *p << "\n";

    std::cout << "Value of y: " << x << "\n";
    std::cout << "Value of y through pointer q: " << *q << "\n\n";
    
    std::cout << "You can also check the addresses of the pointers" << "\n";
    
    std::cout << "Address stored in pointer p: " << p << "\n";       // This points to x
    std::cout << "Address stored in pointer q: " << q << "\n\n";     // This points to y
    
    std::cout << "Point the pointer p to the address of q which points to y" << "\n";
    p = q;           // Point the pointer p to the address of q which points to y

    std::cout << "Value through pointer p: " << *p << "\n";     // This will now print out the value of y, not x as before
    std::cout << "Value through pointer q: " << *q << "\n\n";     // Still points to y
    
    std::cout << "You can also check the addresses of the pointers" << "\n";
    
    std::cout << "Address stored in pointer p: " << p << "\n";     // This will now print out the value of y, not x as before
    std::cout << "Address stored in pointer q: " << q << "\n\n";     // Still points to y

    *p = 42;             // Overwrite the value stored at the address of p. This overwrites y!

    std::cout << "Value of y through pointer p: " << *p << "\n";
    std::cout << "Value of y through pointer q: " << *q << "\n";    

    return 0;
}