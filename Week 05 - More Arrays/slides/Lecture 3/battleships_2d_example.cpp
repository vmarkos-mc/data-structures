// YOU ARE NOT EXPECTED TO UNDERSTAND THIS CODE
// This is an example of using a 2D array to store a grid for a battleship game

#include <iostream>
#include <cstdlib>
#include <ctime>

const int gridSize = 5;
char grid[gridSize][gridSize];
int shipRow, shipCol;

// Initialize the grid
void initializeGrid() {
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            grid[i][j] = '-';
        }
    }
}

// Print the grid
void printGrid() {
    for (int i = 0; i < gridSize; i++) {
        for (int j = 0; j < gridSize; j++) {
            std::cout << grid[i][j] << ' ';
        }
        std::cout << std::endl;
    }
}

// Place the ship randomly
void placeShip() {
    srand(static_cast<unsigned>(time(0)));
    shipRow = rand() % gridSize;
    shipCol = rand() % gridSize;
}

// Check if the player has won
bool checkWin(int guessRow, int guessCol) {
    return guessRow == shipRow && guessCol == shipCol;
}

int main() {
    std::cout << "Welcome to Battleship!" << std::endl;
    initializeGrid();
    placeShip();
    int attempts = 0;

    while (true) {
        printGrid();
        int guessRow, guessCol;

        std::cout << "Enter your guess (row (starts at 0) and column (starts at 0)): \n";
        std::cin >> guessRow >> guessCol;

        if (guessRow < 0 || guessRow >= gridSize || guessCol < 0 || guessCol >= gridSize) {
            std::cout << "Invalid guess. Please enter valid coordinates." << std::endl;
            continue;
        }

        attempts++;

        if (checkWin(guessRow, guessCol)) {
            std::cout << "Congratulations! You sunk the battleship in " << attempts << " attempts." << std::endl;
            grid[guessRow][guessCol] = 'X';
            printGrid();
            break;
        } else {
            std::cout << "You missed!" << std::endl;
            grid[guessRow][guessCol] = 'M';
        }
    }

    return 0;
}
