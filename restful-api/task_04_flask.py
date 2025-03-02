from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary to store users by their username
users = {}

@app.route("/", methods=["GET"])
def home():
    """
    Returns a simple greeting at the root endpoint.
    Matches the pattern of a welcome message from earlier tasks.
    """
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def data():
    """
    Returns a list of existing usernames in JSON.
    Example response: ["john", "jane", ...]
    """
    return jsonify(list(users.keys()))

@app.route("/status", methods=["GET"])
def status():
    """
    Returns a simple 'OK' to indicate the server is running.
    """
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def user_page(username):
    """
    If the user <username> exists in the dictionary, return their details.
    Otherwise, return a 404-style JSON: {"error": "User not found"}.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Create a new user from JSON data in the POST request body.
    Expects at least:
      {
        "username": "johndoe"
      }

    Optionally supports:
      {
        "name": "John",
        "age": 30,
        "city": "New York"
      }

    Returns 400 if there's no JSON or missing username,
    400 if user already exists, or 201 if created successfully.
    """
    # Attempt to parse JSON; (request.json) is a shortcut for request.get_json()
    newuser = request.json
    if not newuser or "username" not in newuser:
        return jsonify({"error": "Username is required"}), 400

    username = newuser["username"].strip().lower()
    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Create a new user entry
    users[username] = {
        "username": username,
        "name": newuser.get("name", ""),
        "age": newuser.get("age", 0),
        "city": newuser.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    # Running in debug mode for development.
    # In production, consider running with a WSGI server like gunicorn.
    app.run(debug=True)
