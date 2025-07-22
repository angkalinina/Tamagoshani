from flask import Flask, jsonify, request
from controller import Controller
from repository import Repository
from time_manager import TimeManager
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

# Игровые компоненты
repo = Repository()
time = TimeManager()
controller = Controller(repo, time)

# Заглушка: используем user_id = 1
USER_ID = 1

@app.route("/state", methods=["GET"])
def get_state():
    controller.tick(USER_ID)
    pet = repo.get_pet(USER_ID)
    return jsonify({
        "hunger": pet.hunger,
        "energy": pet.energy,
        "sleeping": pet.sleeping,
        "refused": pet.refused,
        "state": pet.state
    })

@app.route("/action", methods=["POST"])
def perform_action():
    data = request.get_json()
    action = data.get("type")

    if action == "feed":
        controller.feed(USER_ID)
    elif action == "play":
        controller.play(USER_ID)
    elif action == "sleep":
        controller.sleep(USER_ID)
    elif action == "wake":
        controller.wake_up(USER_ID)
    elif action == "refuse":
        controller.refuse(USER_ID)
    else:
        return jsonify({"error": "Unknown action"}), 400

    return get_state()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
