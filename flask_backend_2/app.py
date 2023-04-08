from flask import Flask, request, jsonify

app = Flask(__name__)

# Dictionary to store user credentials (username: password)
users = {}

# Endpoint for user registration
@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not isinstance(username, str) or not isinstance(password, str):
            return jsonify({"error": "Invalid input. Please provide a string for both username and password."}), 400

        if username in users:
            return jsonify({"error": "Username already exists. Please choose a different one."}), 400

        users[username] = password
        return jsonify({"success": f"User {username} registered successfully."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint for user login
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data['username']
        password = data['password']

        if not isinstance(username, str) or not isinstance(password, str):
            return jsonify({"error": "Invalid input. Please provide a string for both username and password."}), 400

        if username in users and users[username] == password:
            return jsonify({"success": f"Access granted for user {username}."}), 200
        else:
            return jsonify({"error": "Access denied. Invalid username or password."}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
