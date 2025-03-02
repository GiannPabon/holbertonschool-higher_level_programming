from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with an empty dictionary of users
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def data():
    """
    Return a list of user objects, e.g.:
    [
      {"username": "john", "name": "John", "age": 30, "city": "New York"},
      ...
    ]
    """
    # Convert the users dict values into a list of dicts
    all_users = list(users.values())
    return jsonify(all_users)

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def user_page(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects JSON with at least 'username', e.g.:
    {
      "username": "john",
      "name": "John",
      "age": 25,
      "city": "New York"
    }
    """
    newuser = request.get_json(silent=True)
    if not newuser:
        return jsonify({"error": "No data provided"}), 400

    if "username" not in newuser:
        return jsonify({"error": "Username is required"}), 400

    username = newuser["username"]

    # If this username is already in the dict, return a 400 with a specific message
    if username in users:
        return jsonify({"error": "Username already exists"}), 400

    # Convert 'age' to int if provided
    try:
        age = int(newuser.get("age", 0))
    except ValueError:
        age = 0

    # Create the user object
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
