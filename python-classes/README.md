# Python - Classes and Objects

## Description
This project focuses on understanding and implementing fundamental concepts of Object-Oriented Programming (OOP) in Python. Through a series of exercises, you will learn how to create classes, manage attributes, and implement methods while adhering to Pythonic best practices.

## Learning Objectives
By the end of this project, you should be able to explain:

### General
- What is OOP (Object-Oriented Programming).
- The concept of "first-class everything" in Python.
- What is a class and how to define it.
- What is an object and an instance.
- The difference between a class and an object or instance.
- What is an attribute and how to use it.
- Public, protected, and private attributes and their purposes.
- The purpose and usage of `self`.
- What is a method and how to define it.
- The role of the special `__init__` method and how to use it.
- Concepts of Data Abstraction, Data Encapsulation, and Information Hiding.
- What is a property in Python.
- The difference between an attribute and a property.
- The Pythonic way to write getters and setters.
- How to dynamically create new attributes for existing instances of a class.
- How to bind attributes to objects and classes.
- Understanding the `__dict__` attribute of a class and/or instance.
- How Python finds the attributes of an object or class.
- How to use the `getattr` function.

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- All files should end with a new line.
- The first line of all Python files must be:
  ```python
  #!/usr/bin/python3
  ```
- A `README.md` file at the root of the project folder is mandatory.
- Your code must comply with `pycodestyle` (version 2.7.*).
- All files must be executable.
- Each module, class, and method must contain proper documentation (docstrings).

## Tasks
### Mandatory

#### 0. My First Square
- **File:** `0-square.py`
- Write an empty class `Square` that defines a square.
- **Usage:**
  ```bash
  ./0-main.py
  ```

#### 1. Square with Size
- **File:** `1-square.py`
- Define a square with a private instance attribute `size`.
- Instantiation with size (no type/value verification).

#### 2. Size Validation
- **File:** `2-square.py`
- Add validation to ensure `size` is an integer and ≥ 0.
- Raise `TypeError` and `ValueError` where applicable.

#### 3. Area of a Square
- **File:** `3-square.py`
- Add a public instance method `area` that returns the current square area.

#### 4. Access and Update Private Attribute
- **File:** `4-square.py`
- Add a getter and setter for `size` using the `@property` decorator.
- Include validation in the setter.

#### 5. Printing a Square
- **File:** `5-square.py`
- Add a public instance method `my_print` that prints the square with the `#` character.
- Prints an empty line if `size` is 0.

#### 6. Coordinates of a Square
- **File:** `6-square.py`
- Add a private instance attribute `position` with validation.
- Modify `my_print` to consider `position` when printing.

## Repository Structure
```
python-classes/
├── 0-square.py
├── 1-square.py
├── 2-square.py
├── 3-square.py
├── 4-square.py
├── 5-square.py
├── 6-square.py
├── README.md
```

## Author
- **Giann Pabon**  
  - [LinkedIn](https://www.linkedin.com/in/giannpabon/)  
  - [GitHub](https://github.com/GiannPabon)

