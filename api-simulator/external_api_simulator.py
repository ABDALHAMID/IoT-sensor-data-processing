from flask import Flask, jsonify
import random
from datetime import datetime

app = Flask(__name__)

NUM_MACHINES = 10  # Change to simulate more/less

def generate_machine_data(machine_id):
    return {
        "machine_id": f"machine_{machine_id}",
        "temperature": round(random.uniform(20.0, 100.0), 2),
        "vibration": round(random.uniform(0.0, 1.5), 2),
        "status": random.choice(["OK", "WARNING", "ERROR"]),
        "timestamp": datetime.utcnow().isoformat(),
        "runtime_hours": round(random.uniform(100, 10000), 1),
        "location": f"factory_{random.randint(1, 3)}"
    }

@app.route("/machines", methods=["GET"])
def get_all_machines():
    return jsonify([generate_machine_data(i) for i in range(1, NUM_MACHINES + 1)])

@app.route("/machine/<int:id>", methods=["GET"])
def get_one_machine(id):
    if 1 <= id <= NUM_MACHINES:
        return jsonify(generate_machine_data(id))
    else:
        return jsonify({"error": "Machine not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)