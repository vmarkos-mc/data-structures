#include <iostream>
#include <bitset>
#include <iomanip>

int main() {
    int numbers[] = {34, 62, 99, 1, -6, 12};
    int arraySize = sizeof(numbers) / sizeof(numbers[0]);

    std::cout << "Element Address" << std::setw(21) << "Element" << std::setw(33) << "Bytes Contents (8-bit binary)" << std::endl;

    for (int i = 0; i < arraySize; ++i) {
        // Print the address of the element in the 1D array
        std::cout << &numbers[i] << std::setw(20) << numbers[i] << std::setw(14);
        
        // Print the contents of each byte within the element as 8-bit binary
        unsigned char* bytePtr = reinterpret_cast<unsigned char*>(&numbers[i]);
        for (int j = 0; j < sizeof(int); ++j) {
            std::cout << std::bitset<8>(bytePtr[j]) << "  ";
        }

        std::cout << std::endl;
    }
    std::cout << "\n\nREMEMBER THAT THE BINARY STRING IS STORED IN LITTLE ENDIAN ORDER - TO CONVERT IT TO A BINARY STRING WRITE THE BYTES IN REVERSE" << std::endl;
    
    std::cout << "\n\nE.g. \n00110100  01001010  00000001  00000000\n" << "00000000  00000001  01001010  00110100 = 84532" << std::endl;
    
    return 0;
}