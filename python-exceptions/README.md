# Python - Exceptions

## Description

This project covers exception handling in Python, focusing on handling errors and exceptions effectively. You will learn how to use `try`, `except`, `finally`, and `raise` to manage runtime errors in Python programs.

## Learning Objectives

By the end of this project, you should be able to:

- Explain why Python programming is awesome
- Differentiate between errors and exceptions
- Understand exceptions and how to use them
- Identify when to use exceptions
- Correctly handle exceptions in Python
- Explain the purpose of catching exceptions
- Raise built-in exceptions
- Implement clean-up actions after exceptions

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on **Ubuntu 20.04 LTS** using **Python 3.8.5**
- Each file must end with a new line
- The first line of all Python scripts must be `#!/usr/bin/python3`
- A `README.md` file at the root of the project is **mandatory**
- Code must follow `pycodestyle` (version `2.7.*`)
- All files must be executable
- The length of files will be tested using `wc`

## Tasks

### 0. Safe list printing

**File:** `0-safe_print_list.py`

- Function: `safe_print_list(my_list=[], x=0)`
- Prints `x` elements of `my_list`
- Uses `try`/`except` to handle errors
- Returns the actual number of elements printed

### 1. Safe printing of an integers list

**File:** `1-safe_print_integer.py`

- Function: `safe_print_integer(value)`
- Prints an integer using `{:d}.format()`
- Uses `try`/`except` to handle errors
- Returns `True` if `value` is an integer, otherwise `False`

### 2. Print and count integers

**File:** `2-safe_print_list_integers.py`

- Function: `safe_print_list_integers(my_list=[], x=0)`
- Prints the first `x` elements that are integers
- Uses `try`/`except` to handle errors
- Returns the actual number of integers printed

### 3. Integers division with debug

**File:** `3-safe_print_division.py`

- Function: `safe_print_division(a, b)`
- Divides `a` by `b`
- Uses `try`/`except`/`finally` to print `Inside result:` with the division result
- Returns the result or `None` if division is not possible

### 4. Divide a list

**File:** `4-list_division.py`

- Function: `list_division(my_list_1, my_list_2, list_length)`
- Divides elements of `my_list_1` by `my_list_2`
- Handles errors such as type mismatch, division by zero, and index out of range
- Returns a new list with the results

### 5. Raise exception

**File:** `5-raise_exception.py`

- Function: `raise_exception()`
- Raises a `TypeError` exception

### 6. Raise a message

**File:** `6-raise_exception_msg.py`

- Function: `raise_exception_msg(message="")`
- Raises a `NameError` exception with a given message

## Repository Structure

```
📂 holbertonschool-higher_level_programming
 ├── 📂 python-exceptions
 │   ├── 0-safe_print_list.py
 │   ├── 1-safe_print_integer.py
 │   ├── 2-safe_print_list_integers.py
 │   ├── 3-safe_print_division.py
 │   ├── 4-list_division.py
 │   ├── 5-raise_exception.py
 │   ├── 6-raise_exception_msg.py
 │   ├── README.md
```

## Usage

Run each script with:

```bash
./<script_name.py>
```

Ensure the scripts have execution permissions:

```bash
chmod +x <script_name.py>
```

## Author

**GitHub:** [Giann Pabon](https://github.com/GiannPabon)


**LinkedIn:** [Giann Pabon](https://www.linkedin.com/in/giannpabon/)

This project is part of Holberton School's higher-level programming curriculum.


