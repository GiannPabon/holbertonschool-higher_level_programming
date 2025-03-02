#!/usr/bin/env python3
"""
Task 4: Simple API using Flask (UPDATED to handle form data)
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory dictionary of users
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    # Return a list of all usernames
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
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
    # Try to parse JSON first
    data = request.get_json(silent=True)
    if data is None:
        # If no JSON, fall back to form data
        data = request.form.to_dict()

    # If still no data or empty
    if not data:
        return jsonify({"error": "Bad request, no data provided"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check for duplicate
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Create the user
    # Convert age to int if it exists, or default to 0
    try:
        age = int(data.get("age", 0))
    except ValueError:
        age = 0

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": age,
        "city": data.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    # Debug mode shows more info if something goes wrong
    app.run(debug=True)

