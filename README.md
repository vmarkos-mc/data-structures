# Data Structures: Introduction using Python and C

This repository provides an introductory course on fundamental **Data Structures**, implemented using both **Python** and **C**. The course is designed to explain how basic and advanced data structures work under the hood, covering topics from theoretical concepts to practical, efficient implementation.

The dual-language approach allows for exploring high-level abstractions in Python alongside the low-level memory management details in C.

## Table of Contents

* [Overview](#️-data-structures-introduction-using-python-and-c)
* [Repository Structure](#repository-structure)
* [Getting Started](#getting-started)
* [Contributing](#contributing)
* [License](#license)

## Repository Structure

The content is broken down into weekly modules. Each module folder contains lecture materials, as well as code implementations in both C and Python.

| Folder | Description |
| :--- | :--- |
| `Week 01 - Introduction` | Covers an overview of Data Structures, their importance, Big O notation for complexity analysis, and introduction to implementation in both C and Python. |
| `LICENSE` | The MIT License for this project. |
| ... | *More weekly modules will cover structures like Linked Lists, Stacks, Queues, Trees, Graphs, and Hash Tables.* |

## Getting Started

To utilize all the code in this repository, you will need a compiler for C and the Python interpreter.

### Prerequisites

* **Python 3.x:** For running the high-level implementations.
* **C Compiler:** Such as GCC or Clang, for compiling the C implementations.

### Running the Code

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/vmarkos-mc/data-structures.git](https://github.com/vmarkos-mc/data-structures.git)
    cd data-structures
    ```

2.  **To run Python files:**
    Navigate to the relevant week and execute the script:
    ```bash
    python Week\ 01\ -\ Introduction/python_example.py
    ```
    (Replace `python_example.py` with the specific file name.)

3.  **To run C files (Compilation):**
    Navigate to the relevant folder, compile the source, and then run the executable:
    ```bash
    # Example using GCC:
    cd Week\ 01\ -\ Introduction
    gcc -o c_example c_example.c
    ./c_example
    ```
    (Replace `c_example.c` and `c_example` with the specific file names.)

## Contributing

We welcome contributions! If you have optimized implementations, improved documentation, or spot any issues, please check the [issues page](https://github.com/vmarkos-mc/data-structures/issues) or submit a pull request.

1.  **Fork** the repository.
2.  **Create** your feature branch (`git checkout -b feature/improved-linked-list`).
3.  **Commit** your changes (`git commit -m 'Optimized C implementation of Linked List'`).
4.  **Push** to the branch (`git push origin feature/improved-linked-list`).
5.  **Open a Pull Request**.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
