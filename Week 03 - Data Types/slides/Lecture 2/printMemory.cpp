// You can run this here - https://www.programiz.com/cpp-programming/online-compiler/

#include <iostream>

// Function to print the binary representation of a value
template <typename T> void printBinaryRepresentation(const T &value) {
  const unsigned char *p = reinterpret_cast<const unsigned char *>(&value);
  int numBytes = sizeof(value);

  for (int i = numBytes - 1; i >= 0; i--) {
    std::cout << (void *)(p + i) << " "; // Print the address pointed to by p
    for (int j = 7; j >= 0; j--) {
      std::cout << ((p[i] >> j) & 1);
    }
    std::cout << std::endl;
  }

  // Print the binary representation of each byte in little-endian order
  std::cout << "\nThe full binary string is therefore:\n";
  for (int i = numBytes - 1; i >= 0; i--) {
    for (int j = 7; j >= 0; j--) {
      std::cout << ((p[i] >> j) & 1);
    }
  }

  std::cout << "\n" << std::endl;
}

int main() {

  // Print the binary representation of each byte in big-endian order
  std::cout << "Print the binary representation of each byte in big-endian "
               "order...\n\n";

  // Test the printBinaryRepresentation function with different data types
  int i = 232;
  bool b = true;
  char c = 'a';
  // float f = 85.125;
  // double d = 85.125;

  std::cout << "int i = 232 -----\n";
  printBinaryRepresentation(i);
  std::cout << "bool b = true -----\n";
  printBinaryRepresentation(b);
  std::cout << "char c = 'a' -----\n";
  printBinaryRepresentation(c);

  return 0;
}
