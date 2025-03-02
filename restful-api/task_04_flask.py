#!/usr/bin/env python3
"""
Task 4: Develop a Simple API using Python with Flask
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# Initially empty, so "Test the data route of the API when no users are added" passes
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def data():
    """
    Returns a list of usernames (keys in the 'users' dict).
    Example response when a user named 'john' exists: ["john"]
    """
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def user_page(username):
    """
    If a user exists under 'username', returns their details.
    Otherwise, returns {"error": "User not found"} with 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects JSON with at least 'username'.
    If 'username' key is missing, returns a 400 with:
        {"error": "Username is required"}
    If username already exists, returns a 400 with:
        {"error": "Username already exists"}
    Otherwise, adds the user and returns 201 with:
        {"message": "User added", "user": {...}}
    """
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Create or store the user object
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    # Default Flask port is 5000. Debug is optional.
    app.run(debug=True)
