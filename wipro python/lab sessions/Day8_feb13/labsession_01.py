from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

EXTERNAL_API = "https://videogamedb.uk/api/v2/videogame"

@app.route("/")
def home():
    return "My Custom Video Game API Server"

@app.route("/games", methods=["GET"])
def get_games():
    try:
        response = requests.get(EXTERNAL_API)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "error": "Failed to fetch data",
                "status_code": response.status_code
            }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/gamespost", methods=["POST"])
def create_game():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No JSON data provided"}), 400

        # Send data to external API
        response = requests.post(EXTERNAL_API, json=data)

        return jsonify({
            "external_status": response.status_code,
            "external_response": response.json()
        }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

@app.route("/gamesput/<int:id>", methods=["PUT"])
def update_game(id):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No JSON data provided"}), 400
        response = requests.put(f"{EXTERNAL_API}/{id}", json=data)
        return jsonify({
            "external_status": response.status_code,
            "external_response": response.text
        }), response.status_code

    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)