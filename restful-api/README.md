# RESTful API Project

This project covers key topics in creating and interacting with RESTful APIs. By working through each task, you will learn:

- **Task 0**: HTTP/HTTPS basics  
- **Task 1**: Consuming APIs with curl  
- **Task 2**: Consuming and processing API data with Python `requests`  
- **Task 3**: Building a simple API with `http.server`  
- **Task 4**: Building a simple API with Flask  
- **Task 5**: API security and authentication (Basic Auth, JWT)

---

## File Structure

```plaintext
restful-api
├── README.md
├── task_00_http_basics.md
├── task_01_curl.md
├── task_02_requests.py
├── task_03_http_server.py
├── task_04_flask.py
└── task_05_basic_security.py
```

### task_00_http_basics.md
Contains explanations on HTTP vs. HTTPS, common request methods, and status codes.

### task_01_curl.md
Demonstrates how to use `curl` to interact with a public API (JSONPlaceholder).

### task_02_requests.py
Shows how to fetch and save data from an API using Python’s `requests` library.  
(Includes a `main` guard at the bottom so you can run it directly.)

### task_03_http_server.py
Implements a minimal web server using Python’s `http.server` module.

### task_04_flask.py
Implements a simple RESTful API using the Flask framework.

### task_05_basic_security.py
Demonstrates API security with Basic Auth and JWT (using `Flask-HTTPAuth` and `Flask-JWT-Extended`).

---

## Usage

1. **Task 0 and Task 1**  
   Refer to the `.md` files directly for instructions and theory.

2. **Task 2**  
   ```bash
   pip install requests
   python3 task_02_requests.py
   ```
   - You’ll see the titles of each post printed in the console.  
   - A `posts.csv` file will be generated with columns `id`, `title`, and `body`.

3. **Task 3**  
   ```bash
   python3 task_03_http_server.py
   ```
   - By default, the server starts on **port 8000**.  
   - Visit `http://localhost:8000/` for a simple greeting.  
   - `http://localhost:8000/data` returns JSON data.  
   - `http://localhost:8000/status` returns "OK".  
   - Any other route returns a 404.

4. **Task 4**  
   ```bash
   pip install Flask
   python3 task_04_flask.py
   ```
   - Starts a Flask server on **port 5000** by default.  
   - `http://localhost:5000/` → "Welcome to the Flask API!"  
   - `http://localhost:5000/data` → Lists all usernames.  
   - `http://localhost:5000/users/<username>` → Provides details for the given username (e.g., "john").  
   - `POST http://localhost:5000/add_user` → Adds a new user when you provide JSON data.

5. **Task 5**  
   ```bash
   pip install flask_httpauth flask_jwt_extended
   python3 task_05_basic_security.py
   ```
   - Server defaults to **port 5001**.  
   - **Basic Auth**: `GET /basic-protected` requires a valid username & password (e.g., `user1` / `password`).  
   - **JWT**:  
     - `POST /login` with `{"username": "...", "password": "..."}` returns a JWT token if valid.  
     - `GET /jwt-protected` requires a valid token in the `Authorization` header.  
     - `GET /admin-only` is restricted to users with an `"admin"` role.

---

## Author

**Giann Pabon**  
- [GitHub](https://github.com/GiannPabon)  
- [LinkedIn](https://www.linkedin.com/in/giannpabon/)  
