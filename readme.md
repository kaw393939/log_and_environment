# Project: Command Pattern and Plugins Homework 5

## Introduction

This project focuses on the development of an interactive command-line application that operates continuously, transitioning from a single-execution script to a fully functional application. Through this assignment, you will explore the command pattern, learn how to dynamically load commands using a simple plugin architecture, and understand the appropriate use of exceptions versus conditional statements to manage invalid data inputs. This unit lays the foundational skills for application development, preparing you for the midterm project, which requires a thorough explanation of your program's architecture, design patterns, and functionality.

## Project Enhancements from Assignment 4

Incorporate the functionalities discussed in the lecture videos to your previous assignment. This includes transforming your calculator program into an interactive application using the command pattern and REPL (Read, Evaluate, Print, Loop) principles.

### Submission Requirements

1. **Initial Setup:**
   - Watch the lecture on the main/command branch, which covers REPL and the command pattern. [Instructor Video: Command Pattern Lecture](https://youtu.be/3DVUN091T5g). Integrate these concepts with your existing program to add four basic commands: add, subtract, multiply, and divide, making your calculator interactive.

2. **(Bonus) Implement a Menu Command:**
   - Create a menu command that displays available commands from the command dictionary at the application's start and when the user types "menu." This is a self-guided challenge to deepen your understanding of dynamic command integration.

3. **Testing and Code Coverage:**
   - With the calculator commands integrated, update and expand your tests to achieve 100% test coverage, ensuring your program's functionality is fully verified.

4. **Plugin Architecture:**
   - View the lecture on implementing plugins [Instructor Video: Plugins Lecture](https://youtu.be/c2PmjazGW2w). Learn to refactor your program to automatically load plugins, facilitating easy command additions without manual updates.

5. **(Bonus) Explore Multiprocessing Capabilities:**
   - Investigate adding multiprocessing features to enable commands/plugins to run on separate cores. This enhancement is a forward-looking feature that prepares your application for future scalability and performance improvements.

## Grading Rubric (Total: 100 Points)

- **Testing (50 Points):**
  - Comprehensive test coverage near 100% average coverage: 50 Points

- **Functionality (50 Points):**
  - Implementation of command pattern and REPL: 10 Points
  - Interactive calculator commands (add, subtract, multiply, divide): 20 Points
  - Successful plugin architecture integration for dynamic command loading: 20 
Ensure that the functionality aligns with the requirements and demonstrates the effective use of the command pattern and plugin architecture as outlined in the instructor videos.

## Recommended Viewing

To complement the project work, the following videos are highly recommended:

1. [Python Loop Performance](https://www.youtube.com/watch?v=Qgevy75co8c) - Insights into loop efficiency.
2. [Habits of The Good Programmer](https://www.youtube.com/watch?v=q1qKv5TBaOA&t=2s) - Design patterns and best practices.
3. [Global Interpreter Lock and Multicore Issues in Python](https://www.youtube.com/watch?v=m4zDBk0zAUY) - Python concurrency explained by its inventor.
4. [Design Patterns Explained](https://www.youtube.com/watch?v=tv-_1er1mWI) - General programming design patterns.
5. [5 Patterns in Python](https://www.youtube.com/watch?v=YMAwgRwjEOQ) - Applying patterns in Python.

## Project Setup

1. Clone the repository.
2. CD into the project folder.
3. Create and activate the virtual environment (VE).
4. Install the required libraries.

## Testing Commands

- Run all tests with `pytest`.
- To test a specific file, use `pytest tests/test_main.py`.
- For linting and coverage, `pytest --pylint --cov` commands can be used separately.

## Installed Libraries

1. [Pytest](https://docs.pytest.org/en/8.0.x/)
2. [Faker](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)

## Adding a Library

1. Ensure you're in the correct VE; if unsure, run "deactivate".
2. Activate the VE.
3. Update the requirements file with `pip freeze > requirements.txt`.

