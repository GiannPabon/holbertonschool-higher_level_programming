# Python - Object-Relational Mapping

## Project Overview

This project focuses on connecting Python with MySQL databases using two different approaches: direct SQL queries with the `MySQLdb` module and Object-Relational Mapping (ORM) with the `SQLAlchemy` module. The goal is to understand how to interact with databases in Python and to appreciate the advantages of using an ORM.

## Curriculum

- **Course**: [C#25] Foundations v2 - Part 2
- **Average Score**: 78.77%
- **Project Badge**: 0%
- **Level**: Amateur
- **Author**: Guillaume

## Background Context

In this project, you will learn how to:

1. Connect to a MySQL database from a Python script.
2. Execute SQL queries to retrieve and manipulate data.
3. Use SQLAlchemy to abstract database interactions through Python classes and objects.

## Requirements

- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: 3.8.5
- **MySQL Version**: 8.0.x
- **MySQLdb Version**: 2.0.x
- **SQLAlchemy Version**: 1.4.x

### General Requirements

- All files must be executable.
- Each file should end with a new line.
- The first line of all files should be `#!/usr/bin/python3`.
- A `README.md` file is mandatory at the root of the project folder.
- Code must adhere to `pycodestyle` (version 2.7.*).
- All modules, classes, and functions must have proper documentation.

## Installation

### MySQL 8.0 on Ubuntu 20.04 LTS

```bash
sudo apt update
sudo apt install mysql-server
mysql --version
```

### Install MySQLdb Module

```bash
sudo apt-get install python3-dev
sudo apt-get install libmysqlclient-dev
sudo apt-get install zlib1g-dev
sudo pip3 install mysqlclient
```

### Install SQLAlchemy Module

```bash
sudo pip3 install SQLAlchemy
```

## Learning Objectives

By the end of this project, you should be able to:

- Explain how to connect to a MySQL database from a Python script.
- Perform SELECT and INSERT operations in a MySQL table using Python.
- Understand what ORM means and how to map a Python class to a MySQL table.

## Tasks

The project consists of several tasks, each requiring you to write a Python script to perform specific database operations. Below is a brief overview of the tasks:

1. **Get all states**: List all states from the database.
2. **Filter states**: List states with names starting with 'N'.
3. **Filter states by user input**: Display states matching a user-provided name.
4. **SQL Injection**: Write a safe version of the previous task to prevent SQL injection.
5. **Cities by states**: List all cities from a specific database.
6. **All states via SQLAlchemy**: List all State objects using SQLAlchemy.
7. **Add a new state**: Insert a new state into the database.
8. **Update a state**: Change the name of a state in the database.
9. **Delete states**: Remove states containing the letter 'a'.
10. **Cities in state**: Create a City class and fetch cities by state.

For detailed instructions on each task, please refer to the individual Python scripts in the repository.

## Resources

- [Object-relational mappers](https://docs.sqlalchemy.org/en/14/orm/)
- [MySQLdb documentation](https://mysqlclient.readthedocs.io/)
- [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/14/)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)

## Author

* **Gian Pabon**
    * GitHub: [https://github.com/GiannPabon](https://github.com/GiannPabon)
    * LinkedIn: [https://www.linkedin.com/in/giannpabon/](https://www.linkedin.com/in/giannpabon/)
