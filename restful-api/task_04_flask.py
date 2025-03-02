from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary of users
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    """
    Return a list of *all user objects*, not just the keys.
    Example:
    [
      {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
      }
    ]
    """
    all_users = list(users.values())
    return jsonify(all_users)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<username>")
def user_page(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects JSON with at least a 'username' field, e.g.:
    {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
    }
    """
    # Attempt to parse JSON
    newuser = request.get_json(silent=True)
    if not newuser:
        return jsonify({"error": "No data provided"}), 400

    # Check if 'username' is present
    if "username" not in newuser:
        return jsonify({"error": "Username is required"}), 400

    username = newuser["username"]
    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Convert 'age' to int (if present), else default to 0
    try:
        age = int(newuser.get("age", 0))
    except ValueError:
        age = 0

    # Create the user dictionary
    users[username] = {
        "username": username,
        "name": newuser.get("name", ""),
        "age": age,
        "city": newuser.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
