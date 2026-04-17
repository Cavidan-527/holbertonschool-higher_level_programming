#!/usr/bin/python3
"""
A simple Flask API that manages a dictionary of users.
It supports GET and POST requests for user data.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# İstifadəçilər yaddaşda lüğət daxilində saxlanılır
users = {}


@app.route("/")
def home():
    """Returns a welcome message for the root URL."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames in the system."""
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """Returns the current status of the API."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Parses JSON data and adds a new user to the dictionary."""
    # JSON-un düzgünlüyünü yoxlayırıq
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "User already exists"}), 409

    # Yeni istifadəçini əlavə edirik
    users[username] = data
    response_data = {
        "message": "User added",
        "user": data
    }
    return jsonify(response_data), 201


if __name__ == "__main__":
    app.run()
