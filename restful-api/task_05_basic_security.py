#!/usr/bin/python3
"""
Flask API implementing Basic Auth, JWT, and Role-based Access Control.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt
)


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Real layihədə gizli saxla
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# İstifadəçi verilənləri
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


# --- Basic Authentication Hissəsi ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username
    return None


@auth.error_handler
def basic_auth_error(status):
    """Ensures Basic Auth returns 401 for all authentication errors."""
    return jsonify({"error": "Unauthorized"}), 401


# --- JWT Error Handlers (401 Tələbi üçün) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


# --- Marşrutlar (Endpoints) ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """Login route that issues a JWT token."""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Role məlumatını tokenin içinə (claims) əlavə edirik
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user['role']}
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based check (Admin only)."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
