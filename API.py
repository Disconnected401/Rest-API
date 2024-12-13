from flask import Flask, jsonify, request, abort
import json

app = Flask(__name__)


users = []

def load_users():
    try:
        with open('users.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_users():
    with open('users.json', 'w') as file:
        json.dump(users, file)

users = load_users()

@app.after_request
def after_request(response):
    if request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
        save_users()
    return response

def generate_id():
    if users:
        return max(user["id"] for user in users) + 1
    return 1

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(404)
    return jsonify(user), 200

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or "name" not in request.json or "lastname" not in request.json:
        abort(400)
    new_user = {
        "id": generate_id(),
        "name": request.json["name"],
        "lastname": request.json["lastname"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user_partial(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(400)
    if not request.json or not any(key in request.json for key in ["name", "lastname"]):
        abort(400)
    user.update({key: value for key, value in request.json.items() if key in ["name", "lastname"]})
    return '', 204

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if not request.json or "name" not in request.json or "lastname" not in request.json:
        abort(400)
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        user = {"id": user_id, "name": request.json["name"], "lastname": request.json["lastname"]}
        users.append(user)
    else:
        user.update({"name": request.json["name"], "lastname": request.json["lastname"]})
    return '', 204

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user["id"] == user_id), None)
    if user is None:
        abort(400)
    users.remove(user)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
