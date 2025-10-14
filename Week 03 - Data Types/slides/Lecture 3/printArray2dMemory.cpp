#include <iostream>
#include <bitset>
#include <iomanip>

int main() {
    int matrix[3][3] = {{6, 2, -3}, {4, 5, 6}, {84532, 0, 10}};
    int numRows = sizeof(matrix) / sizeof(matrix[0]);
    int numCols = sizeof(matrix[0]) / sizeof(matrix[0][0]);

    std::cout << "Element Address" << std::setw(21) << "Element" << std::setw(33) << "Bytes Contents (8-bit binary)" << std::endl;

    for (int row = 0; row < numRows; ++row) {
        for (int col = 0; col < numCols; ++col) {
            // Print the address of the element in the 2D array
            std::cout << &matrix[row][col] << std::setw(20) << matrix[row][col] << std::setw(14);

            // Print the contents of each byte within the element as 8-bit binary
            unsigned char* bytePtr = reinterpret_cast<unsigned char*>(&matrix[row][col]);
            for (int j = 0; j < sizeof(int); ++j) {
                std::cout << std::bitset<8>(bytePtr[j]) << "  ";
            }

            std::cout << std::endl;
        }
        
    }
    std::cout << "\n\nREMEMBER THAT THE BINARY STRING IS STORED IN LITTLE ENDIAN ORDER - TO CONVERT IT TO A BINARY STRING WRITE THE BYTES IN REVERSE" << std::endl;
    
    std::cout << "\n\nE.g. \n00110100  01001010  00000001  00000000\n" << "00000000  00000001  01001010  00110100 = 84532" << std::endl;
    
    return 0;
}