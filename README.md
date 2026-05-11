# OOP Hands-On Assignment

## Objective

This project practices Python object-oriented programming by creating a `Student` class and using common Python data types such as lists, tuples, sets, and dictionaries.

The program creates student objects, stores their grades, calculates averages, retrieves students by email, validates email addresses with regular expressions, and demonstrates basic collection operations.

The exact grades and averages will vary because the program uses `random.randint()`.

## Assignment Parts

### Part 1: Class Definition

The assignment defines a `Student` class with the following attributes:

- `name`: the student's name
- `email`: the student's email address
- `grades`: a list of integer grades

The class includes these methods:

- `add_grade(self, grade)`: adds a grade to the student's grade list
- `average_grade(self)`: returns the student's average grade
- `display_info(self)`: returns formatted student information
- `grades_tuple(self)`: returns the student's grades as a tuple
- `validate_email(self, email)`: validates the student's email using regular expressions

### Part 2: Working with Objects

The script creates three student objects:

- George
- Larry
- Kristina

Each student starts with three randomly generated grades. Two additional grades are added to each student using the `add_grade()` method.

The program then prints each student's information and average grade.

### Part 3: Dictionary and Set Integration

The script creates a dictionary named `student_dict`.

Each student's email is used as the key, and the matching `Student` object is used as the value.

Example:

```python
student_dict = {
    student1.email: student1,
    student2.email: student2,
    student3.email: student3,
}
```

The function `get_student_by_email(email)` safely retrieves a student object using `.get()`.

The function `get_all_unique_grades(students)` creates a set of all unique grades across every student.

### Part 4: Tuple Practice

The `grades_tuple()` method converts a student's grades list into a tuple.

The script demonstrates that tuples are immutable by attempting to change a tuple value inside a `try` / `except` block. When Python raises a `TypeError`, the program catches it and prints a helpful message.

### Part 5: List Operations

The script uses list operations to:

- Remove the last grade from each student's grade list with `.pop()`
- Print the first and last grade for each student
- Print the number of grades each student has with `len()`

The list operations are wrapped in a `try` / `except` block to handle a possible `IndexError`.

### Part 6: Bonus

The bonus requirements are also included.

The program validates each student's email address with the `re` module and this regular expression:

```python
r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
```

This pattern checks for an email format similar to:

```text
name@domain.com
```

The program also counts how many grades are 90 or above across all students using the `get_all_90_above(students)` function.

## Concepts Practiced

- Python classes and objects
- The `__init__` constructor
- Instance methods
- Lists
- Tuples
- Sets
- Dictionaries
- Dictionary lookups with `.get()`
- Set comprehensions
- Regular expressions
- Random number generation
- Exception handling with `try` / `except`

## Project Files

```text
OOPAssignment/
|-- OOP_Hands_On_Assignment.py
|-- README.md
```

## Author

Created by Joseph McDaniel
Github: https://github.com/JoeM10/