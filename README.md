# CS50P Problem Sets

Complete solutions and practice exercises for Harvard's CS50 Introduction to Programming with Python course.

## Overview

This repository contains comprehensive solutions to all CS50P problem sets, along with extensive practice exercises. It covers fundamental to intermediate Python programming concepts and is ideal for learning Python through structured, project-based challenges.

## Tech Stack

- **Language**: Python 3.8+
- **Testing Framework**: pytest
- **Linting**: flake8
- **Package Manager**: pip

## Repository Structure

### Problem Sets (PS0 - PS8)
- **PS0** - Conditionals, Loops, and Functions
- **PS1** - Variables and Functions
- **PS2** - Loops, Strings, and Lists
- **PS3** - Exception Handling, Files, and Regular Expressions
- **PS4** - Libraries and Modules
- **PS5** - Object-Oriented Programming (OOP)
- **PS6** - File I/O and Data Processing
- **PS7** - Testing and Debugging
- **PS8** - Advanced Topics and Final Projects

### Practice Exercises
- **practiceeee** - Sandbox for experimental code and additional practice
  - Contains mini-projects, coding challenges, and learning exercises
  - Includes test suites for validation
  - Topics: bank operations, calculators, string manipulation, etc.

## Topics Covered

- **Core Language**: Variables, data types, operators, control flow
- **Functions**: Definition, parameters, return values, scope
- **Data Structures**: Lists, tuples, dictionaries, sets
- **String Operations**: Manipulation, formatting, regular expressions
- **File Handling**: Reading, writing, processing different file formats
- **Object-Oriented Programming**: Classes, inheritance, polymorphism
- **Exception Handling**: Try-except blocks, custom exceptions
- **Testing**: Unit tests with pytest, test-driven development
- **Libraries**: Working with external modules and packages
- **Advanced Topics**: Decorators, generators, context managers

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

Clone the repository:
```bash
git clone https://github.com/fizaan-ali/CS50P_ProblemSets.git
cd CS50P_ProblemSets
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Problem Sets

Each problem set has its own directory. To run a specific solution:

```bash
python PS1/hello.py
python PS3/mail.py input.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests for a specific problem set:
```bash
pytest PS5/
```

Run tests with verbose output:
```bash
pytest -v
```

### Practice Exercises

Navigate to the practiceeee directory and run individual exercises:
```bash
cd practiceeee
python bank.py
pytest test_bank.py
```

## Code Quality

All code is checked with flake8 for style compliance. To check your code:

```bash
flake8 .
```

## Learning Resources

- Official CS50P Course: https://cs50.harvard.edu/python
- Python Documentation: https://docs.python.org/3/
- PEP 8 Style Guide: https://www.python.org/dev/peps/pep-0008/

## Key Implementations

### String Operations
- Email validation with regex
- String parsing and manipulation
- Text file processing

### Data Structures
- Working with lists and dictionaries
- Sorting and searching algorithms
- Data transformation and aggregation

### Object-Oriented Programming
- Class design and inheritance
- Encapsulation and polymorphism
- Design patterns implementation

### Testing
- Unit tests with pytest
- Test fixtures and parametrization
- Mocking and test isolation

## License

MIT License - See LICENSE file for details

## Author

Fizaan Ali
