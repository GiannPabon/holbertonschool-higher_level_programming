# Python - Data Structures: Lists, Tuples

## Description
This project focuses on understanding and implementing fundamental data structures in Python: **lists** and **tuples**. Through a series of exercises, you will practice manipulating these data structures while adhering to Pythonic best practices.

## Learning Objectives
By the end of this project, you should be able to explain:

### General
- What lists are and how to use them.
- The differences and similarities between strings and lists.
- Common list methods and their applications.
- How to use lists as **stacks** and **queues**.
- List comprehensions and their benefits.
- What tuples are and how to use them.
- When to use tuples versus lists.
- The concept of sequences in Python.
- Tuple packing and unpacking.
- How to use the `del` statement.

## Requirements
### Python Scripts
- All scripts should be written in **Python 3** (version 3.8.5).
- Your code must comply with **pycodestyle** (version 2.7.*).
- The first line of all Python files must be:
  ```python
  #!/usr/bin/python3
  ```
- All files must be **executable**.
- All scripts should end with a **new line**.
- No additional modules may be imported unless specified.

## Tasks
### Mandatory

#### 0. Print a list of integers
- Function: `print_list_integer(my_list=[])`
- Prints each integer from the list on a new line using `str.format()`.
- **File:** `0-print_list_integer.py`

#### 1. Secure access to an element in a list
- Function: `element_at(my_list, idx)`
- Returns the element at `idx`, or `None` if `idx` is out of range.
- **File:** `1-element_at.py`

#### 2. Replace element
- Function: `replace_in_list(my_list, idx, element)`
- Replaces an element in a list at a given index.
- **File:** `2-replace_in_list.py`

#### 3. Print a list of integers... in reverse!
- Function: `print_reversed_list_integer(my_list=[])`
- Prints a list of integers in reverse order.
- **File:** `3-print_reversed_list_integer.py`

#### 4. Replace in a copy
- Function: `new_in_list(my_list, idx, element)`
- Creates a copy of a list and replaces an element at a given index.
- **File:** `4-new_in_list.py`

#### 5. Can you C me now?
- Function: `no_c(my_string)`
- Returns a string with all **'c'** and **'C'** removed.
- **File:** `5-no_c.py`

#### 6. Lists of lists = Matrix
- Function: `print_matrix_integer(matrix=[[]])`
- Prints a matrix of integers.
- **File:** `6-print_matrix_integer.py`

#### 7. Tuples addition
- Function: `add_tuple(tuple_a=(), tuple_b=())`
- Adds two tuples element-wise.
- **File:** `7-add_tuple.py`

#### 8. More returns!
- Function: `multiple_returns(sentence)`
- Returns a tuple with the length of a string and its first character.
- **File:** `8-multiple_returns.py`

#### 9. Find the max
- Function: `max_integer(my_list=[])`
- Finds and returns the maximum integer in a list.
- **File:** `9-max_integer.py`

#### 10. Only by 2
- Function: `divisible_by_2(my_list=[])`
- Returns a list indicating whether each number in the input list is divisible by 2.
- **File:** `10-divisible_by_2.py`

#### 11. Delete at
- Function: `delete_at(my_list=[], idx=0)`
- Deletes an item at a specific index in a list.
- **File:** `11-delete_at.py`

#### 12. Switch
- Modifies given code to swap values of `a` and `b` in exactly 5 lines.
- **File:** `12-switch.py`

## Repository Structure
```
python-data_structures/
├── 0-print_list_integer.py
├── 1-element_at.py
├── 2-replace_in_list.py
├── 3-print_reversed_list_integer.py
├── 4-new_in_list.py
├── 5-no_c.py
├── 6-print_matrix_integer.py
├── 7-add_tuple.py
├── 8-multiple_returns.py
├── 9-max_integer.py
├── 10-divisible_by_2.py
├── 11-delete_at.py
├── 12-switch.py
├── README.md
```

## Author
- **Giann Pabon**  
  - [LinkedIn](https://www.linkedin.com/in/giannpabon/)  
  - [GitHub](https://github.com/GiannPabon)


