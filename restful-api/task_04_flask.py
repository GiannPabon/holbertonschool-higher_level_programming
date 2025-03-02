from flask import Flask, jsonify, request

app = Flask(__name__)

# Start with NO users in the dictionary
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data", methods=["GET"])
def get_data():
    """
    Return a list of all user dictionaries exactly as they were added.
    Example:
    [
      {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        ...any other fields posted...
      }
    ]
    """
    return jsonify(list(users.values()))

@app.route("/status", methods=["GET"])
def status():
    return "OK"

@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Expects JSON data with at least a 'username' key, e.g.:
    {
      "username": "john",
      "name": "John",
      "age": 25,
      "city": "New York"
    }

    - Returns 400 if no JSON, no username, or username already in use.
    - Returns 201 with a JSON response containing "message" and "user" if successful.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Store the entire JSON dict, so the test sees the exact object posted
    # (including any extra keys the test might send)
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
