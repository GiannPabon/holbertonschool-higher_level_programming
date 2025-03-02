from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, get_jwt_identity, jwt_required, create_access_token
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# In-memory database of users (for demonstration)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# Configure secret key for JWT
app.config["JWT_SECRET_KEY"] = "your_secret_key"  # Replace in production
jwt = JWTManager(app)

# -------------------------------------------------------------------
# BASIC AUTH
# -------------------------------------------------------------------
@auth.verify_password
def verify_password(username, password):
    """
    Called by @auth.login_required to check username & password.
    Returns the user dictionary if valid, or None if invalid.
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    """
    Basic Auth route.
    Returns "Basic Auth: Access Granted" if correct credentials are provided.
    Else returns a 401 Unauthorized automatically.
    """
    return "Basic Auth: Access Granted"

# -------------------------------------------------------------------
# JWT AUTH
# -------------------------------------------------------------------
@app.route("/login", methods=["POST"])
def login():
    """
    Expects JSON:
      {
        "username": "...",
        "password": "..."
      }
    If valid, returns an "access_token".
    If missing or invalid, returns an error JSON.
    """
    # Pull username and password from request JSON
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    # Check user credentials
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Create a JWT token with user identity (username & role)
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401

@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """
    JWT-protected route.
    Requires a valid token passed as an Authorization header:
      Authorization: Bearer <token>
    """
    return "JWT Auth: Access Granted"

@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Route restricted to 'admin' role.
    If the token identity has role != 'admin', returns 403.
    """
    identity = get_jwt_identity()  # e.g. {"username": "admin1", "role": "admin"}
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

# -------------------------------------------------------------------
# CUSTOM JWT ERROR HANDLERS
# -------------------------------------------------------------------
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    When JWT is missing or invalid, return a 401 with a JSON error.
    """
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    When the token is invalid in some way, return a 401.
    """
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    When the token is valid but expired, return a 401.
    """
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    If the token is revoked, also return a 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    If a route requires a 'fresh' token but receives a non-fresh one, return 401.
    """
    return jsonify({"error": "Fresh token required"}), 401

# -------------------------------------------------------------------
# RUN THE APP
# -------------------------------------------------------------------
if __name__ == "__main__":
    app.run()
