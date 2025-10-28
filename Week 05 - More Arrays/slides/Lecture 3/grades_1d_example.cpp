// YOU ARE NOT EXPECTED TO UNDERSTAND THIS CODE
// This is an example of using a 1D array to store grades for 5 students

#include <iostream>

int main() {
    const int numStudents = 5;
    int grades[numStudents];

    // Input: Enter grades for each student
    for (int i = 0; i < numStudents; i++) {
        std::cout << "Enter the grade for student " << i + 1 << ": ";
        std::cin >> grades[i];
    }

    // Output: Display the entered grades
    std::cout << "Entered Grades:" << std::endl;
    for (int i = 0; i < numStudents; i++) {
        std::cout << "Student " << i + 1 << ": " << grades[i] << std::endl;
    }

    // Calculate the average grade
    int sum = 0;
    for (int i = 0; i < numStudents; i++) {
        sum += grades[i];
    }
    double average = static_cast<double>(sum) / numStudents;

    // Output: Display the average grade
    std::cout << "Average Grade: " << average << std::endl;

    return 0;
}
