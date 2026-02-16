from flask import Flask,jsonify, request
app = Flask(__name__)
@app.route("/")
def home():
    return "Welcome to flask web server!"
@app.route('/users', methods=['GET'])
def get_user():
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})
@app.route("/users", methods=["POST"])
def add_users():
    data = request.get_json()
    return jsonify(data), 201
@app.route("/users/<int:id>", methods=["PUT"])
def update_users(id):
    return jsonify({"Message": f"user {id} is updated"})
@app.route("/users/<int:id>", methods=["DELETE"])
def delete_users(id):
    return jsonify({"Message": f"user {id} is deleted"})
@app.route("/users/<int:id>", methods=["PATCH"])
def patch_users(id):
    data = request.get_json()
    return jsonify({"Message": "user updated partially",
                    "user_id": id,
                    "email": data})
if __name__ == "__main__":
    app.run(debug = True)
