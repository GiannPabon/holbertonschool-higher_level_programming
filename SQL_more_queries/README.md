SQL - More queries

This project focuses on advanced SQL queries and database management in MySQL. It covers creating users, managing privileges, working with constraints, and retrieving data from multiple tables using joins and subqueries.

## Learning Objectives

By completing this project, you should be able to:

* **General:**
    * Create new MySQL users.
    * Manage user privileges for databases and tables.
    * Understand and use `PRIMARY KEY`, `FOREIGN KEY`, `NOT NULL`, and `UNIQUE` constraints.
    * Retrieve data from multiple tables in a single query.
    * Work with subqueries.
    * Understand and use `JOIN` and `UNION`.

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

### 0. My privileges!

* Write a script (`0-privileges.sql`) that lists all privileges of MySQL users `user_0d_1` and `user_0d_2` on localhost.

### 1. Root user

* Write a script (`1-create_user.sql`) that creates the MySQL server user `user_0d_1` with all privileges and password `user_0d_1_pwd`.

### 2. Read user

* Write a script (`2-create_read_user.sql`) that creates database `hbtn_0d_2` and user `user_0d_2` with SELECT privilege on `hbtn_0d_2` and password `user_0d_2_pwd`.

### 3. Always a name

* Write a script (`3-force_name.sql`) that creates table `force_name` with `name` not null.

### 4. ID can't be null

* Write a script (`4-never_empty.sql`) that creates table `id_not_null` with `id` having a default value of 1.

### 5. Unique ID

* Write a script (`5-unique_id.sql`) that creates table `unique_id` with `id` unique and default value of 1.

### 6. States table

* Write a script (`6-states.sql`) that creates database `hbtn_0d_usa` and table `states` with auto-generated primary key `id`.

### 7. Cities table

* Write a script (`7-cities.sql`) that creates table `cities` with foreign key `state_id` referencing `states.id`.

### 8. Cities of California

* Write a script (`8-cities_of_california_subquery.sql`) that lists cities of California using a subquery.

### 9. Cities by States

* Write a script (`9-cities_by_state_join.sql`) that lists cities with state names using a join.

### 10. Genre ID by show

* Write a script (`10-genre_id_by_show.sql`) that lists shows with genre IDs.

### 11. Genre ID for all shows

* Write a script (`11-genre_id_all_shows.sql`) that lists all shows with genre IDs, including NULL for shows without genres.

### 12. No genre

* Write a script (`12-no_genre.sql`) that lists shows without a genre linked.

### 13. Number of shows by genre

* Write a script (`13-count_shows_by_genre.sql`) that lists genres and the number of shows linked to each.

### 14. My genres

* Write a script (`14-my_genres.sql`) that lists all genres of the show Dexter.

### 15. Only Comedy

* Write a script (`15-comedy_only.sql`) that lists all Comedy shows.

### 16. List shows and genres

* Write a script (`16-shows_by_genre.sql`) that lists all shows and their genres, including NULL for shows without genres.

## Author

* **Gian Pabon**
    * GitHub: [https://github.com/GiannPabon](https://github.com/GiannPabon)
    * LinkedIn: [https://www.linkedin.com/in/giannpabon/](https://www.linkedin.com/in/giannpabon/)