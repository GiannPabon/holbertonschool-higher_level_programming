from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary
users = {}

@app.route("/")
def home():
    """
    Return a basic greeting at the root endpoint.
    """
    return "Welcome to the Flask API!"

@app.route("/data")
def get_all_users():
    """
    Return a list of all user objects.
    Example:
    [
      {"username": "john", "name": "John", "age": 30, "city": "New York"},
      {"username": "jane", "name": "Jane", "age": 28, "city": "LA"}
    ]
    """
    return jsonify(list(users.values()))

@app.route("/status")
def status():
    """
    Simple status check.
    """
    return "OK"

@app.route("/users/<username>")
def get_user(username):
    """
    Return user details if they exist, or a 404-style JSON if not.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects JSON like:
    {
        "username": "john",
        "name": "John",
        "age": 25,
        "city": "New York"
    }
    Returns 400 if no username or user already exists.
    Returns 201 with the new user's data if successful.
    """
    # Attempt to parse JSON from the request body
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Check for 'username' field
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicates
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Convert age to int if present; default 0
    try:
        age = int(data.get("age", 0))
    except ValueError:
        age = 0

    # Build the user object
    user_obj = {
        "username": username,
        "name": data.get("name", ""),
        "age": age,
        "city": data.get("city", "")
    }

    # Store it in our dictionary
    users[username] = user_obj

    # Return a 201 Created, with a success message and the new user data
    return jsonify({"message": "User added", "user": user_obj}), 201

if __name__ == "__main__":
    # Run the app in debug mode for clarity
    app.run(debug=True)
