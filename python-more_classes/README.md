# Python - More Classes and Objects

## Description
This project delves deeper into Object-Oriented Programming (OOP) concepts in Python, focusing on class attributes, static and class methods, and the customization of object behavior through special methods. You'll learn how to define and manage classes effectively, making your code more modular and reusable.

## Learning Objectives
By the end of this project, you should be able to explain:

### General
- Why Python programming is awesome
- What is OOP (Object-Oriented Programming)
- The concept of "first-class everything"
- What is a class
- What is an object and an instance
- The difference between a class and an object or instance
- What is an attribute and how to use it
- Public, protected, and private attributes and their purposes
- The purpose and usage of `self`
- What is a method and how to define it
- The role of the special `__init__` method and how to use it
- Concepts of Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property in Python
- The difference between an attribute and a property
- The Pythonic way to write getters and setters
- Special methods `__str__` and `__repr__` and how to use them
- The difference between `__str__` and `__repr__`
- What is a class attribute and how it differs from instance attributes
- What is a class method and how to define it
- What is a static method and how to define it
- How to dynamically create new attributes for existing instances
- How to bind attributes to objects and classes
- Understanding the `__dict__` attribute of a class and/or instance
- How Python locates the attributes of an object or class
- How to use the `getattr` function

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5)
- All files should end with a new line
- The first line of all Python files must be:
  ```python
  #!/usr/bin/python3
  ```
- A `README.md` file at the root of the project folder is mandatory
- Your code must comply with `pycodestyle` (version 2.7.*)
- All files must be executable
- Each module, class, and method must contain proper documentation (docstrings)

## Tasks
### Mandatory

#### 0. Simple Rectangle
- **File:** `0-rectangle.py`
- Write an empty class `Rectangle` that defines a rectangle.

#### 1. Real Definition of a Rectangle
- **File:** `1-rectangle.py`
- Add private instance attributes `width` and `height` with property setters and getters.
- Include validation for type and value constraints.

#### 2. Area and Perimeter
- **File:** `2-rectangle.py`
- Add methods `area` and `perimeter` to compute respective values.

#### 3. String Representation
- **File:** `3-rectangle.py`
- Customize the string representation of the rectangle using the `#` character.

#### 4. Eval is Magic
- **File:** `4-rectangle.py`
- Implement the `__repr__` method to allow recreation of the object using `eval()`.

#### 5. Detect Instance Deletion
- **File:** `5-rectangle.py`
- Add a message "Bye rectangle..." that prints when an instance is deleted.

#### 6. How Many Instances
- **File:** `6-rectangle.py`
- Add a class attribute `number_of_instances` to track the number of active instances.

#### 7. Change Representation
- **File:** `7-rectangle.py`
- Add a class attribute `print_symbol` to customize the rectangle's print symbol.

#### 8. Compare Rectangles
- **File:** `8-rectangle.py`
- Add a static method `bigger_or_equal` to compare rectangles based on area.

#### 9. A Square is a Rectangle
- **File:** `9-rectangle.py`
- Add a class method `square` that returns a new `Rectangle` instance with equal width and height.

## Repository Structure
```
python-more_classes/
├── 0-rectangle.py
├── 1-rectangle.py
├── 2-rectangle.py
├── 3-rectangle.py
├── 4-rectangle.py
├── 5-rectangle.py
├── 6-rectangle.py
├── 7-rectangle.py
├── 8-rectangle.py
├── 9-rectangle.py
├── README.md
```

## Author
- **Giann Pabon**  
  - [LinkedIn](https://www.linkedin.com/in/giannpabon/)  
  - [GitHub](https://github.com/GiannPabon)

