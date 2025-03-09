```markdown
# SQL - Introduction

This project introduces fundamental concepts of SQL (Structured Query Language) and MySQL, a relational database management system. It covers basic database operations, including creating databases and tables, inserting, updating, and deleting data, and querying data using various SQL statements.

## Learning Objectives

By completing this project, you should be able to:

* **General:**
    * Explain what a database is.
    * Explain what a relational database is.
    * Define SQL and MySQL.
    * Create a database in MySQL.
    * Explain DDL (Data Definition Language) and DML (Data Manipulation Language).
    * Create and alter tables.
    * Select data from a table.
    * Insert, update, and delete data.
    * Understand and use subqueries.
    * Use MySQL functions.

## Requirements

* **General:**
    * Allowed editors: `vi`, `vim`, `emacs`.
    * Files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25).
    * Files should end with a new line.
    * SQL queries should have a comment just before them.
    * Files should start with a comment describing the task.
    * SQL keywords should be in uppercase (e.g., `SELECT`, `WHERE`).
    * A `README.md` file is mandatory.
    * The length of files will be tested using `wc`.

## Installation and Setup

### Ubuntu 20.04 LTS

1.  **Update package list:**

    ```bash
    sudo apt update
    ```

2.  **Install MySQL server:**

    ```bash
    sudo apt install mysql-server
    ```

3.  **Check MySQL version:**

    ```bash
    mysql --version
    ```

4.  **Connect to MySQL server:**

    ```bash
    sudo mysql
    ```

## Tasks

### 0. List databases

* Write a script (`0-list_databases.sql`) that lists all databases on your MySQL server.

### 1. Create a database

* Write a script (`1-create_database_if_missing.sql`) that creates the database `hbtn_0c_0` if it doesn't exist.

### 2. Delete a database

* Write a script (`2-remove_database.sql`) that deletes the database `hbtn_0c_0` if it exists.

### 3. List tables

* Write a script (`3-list_tables.sql`) that lists all tables of a specified database.

### 4. First table

* Write a script (`4-first_table.sql`) that creates the table `first_table` in the current database.

### 5. Full description

* Write a script (`5-full_table.sql`) that prints the full description of the table `first_table`.

### 6. List all in table

* Write a script (`6-list_values.sql`) that lists all rows of the table `first_table`.

### 7. First add

* Write a script (`7-insert_value.sql`) that inserts a new row into the `first_table`.

### 8. Count 89

* Write a script (`8-count_89.sql`) that displays the number of records with `id = 89` in `first_table`.

### 9. Full creation

* Write a script (`9-full_creation.sql`) that creates `second_table` and inserts multiple rows.

### 10. List by best

* Write a script (`10-top_score.sql`) that lists all records of `second_table` ordered by score.

### 11. Select the best

* Write a script (`11-best_score.sql`) that lists records with `score >= 10` in `second_table`.

### 12. Cheating is bad

* Write a script (`12-no_cheating.sql`) that updates Bob's score to `10` in `second_table`.

### 13. Score too low

* Write a script (`13-change_class.sql`) that removes records with `score <= 5` in `second_table`.

### 14. Average

* Write a script (`14-average.sql`) that computes the average score of all records in `second_table`.

### 15. Number by score

* Write a script (`15-groups.sql`) that lists the number of records with the same score in `second_table`.

### 16. Say my name

* Write a script (`16-no_link.sql`) that lists all records of the table `second_table` of the database `hbtn_0c_0` in your MySQL server. Don’t list rows where the `name` column does not contain a value.

## Author

* **Gian Pabon**
    * GitHub: [https://github.com/GiannPabon](https://github.com/GiannPabon)
    * LinkedIn: [https://www.linkedin.com/in/giannpabon/](https://www.linkedin.com/in/giannpabon/)
```
