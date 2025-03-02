#!/usr/bin/env python3
"""
Task 4: Simple API using Flask
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# Start with NO existing users
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """
    Return a list of all user objects.

    Example:
    [
      {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
      },
      ...
    ]
    """
    # Convert users dict to a list of user dicts
    all_users = list(users.values())
    return jsonify(all_users)

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    """
    Returns the user object if found,
    or a 404-style JSON if not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects either JSON or form data that includes 'username'.
    E.g., JSON body:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }

    or form data:
    username=alice&name=Alice&age=25&city=San+Francisco
    """
    # Attempt to parse JSON first
    data = request.get_json(silent=True)
    if data is None:
        # If no JSON, fall back to form data
        data = request.form.to_dict()

    if not data:
        return jsonify({"error": "Bad request, no data provided"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Convert age to int if provided
    try:
        age = int(data.get("age", 0))
    except ValueError:
        age = 0

    # Create the user object
    user_obj = {
        "username": username,
        "name": data.get("name", ""),
        "age": age,
        "city": data.get("city", "")
    }

    # Store the user in the dictionary
    users[username] = user_obj

    return jsonify({
        "message": "User added",
        "user": user_obj
    }), 201

if __name__ == "__main__":
    # Running in debug mode for helpful logs
    app.run(debug=True)
