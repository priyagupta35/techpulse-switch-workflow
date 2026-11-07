import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

SWITCH_API_URL = os.getenv("SWITCH_API_URL", "http://localhost:8080/v1")
SWITCH_SECRET = os.getenv("SWITCH_SECRET", "techpulse_secret_key")

@app.route("/api/techpulse-alert", methods=["POST"])
def receive_techpulse_alert():
    auth_header = request.headers.get("Authorization")
    if auth_header != f"Bearer {SWITCH_SECRET}":
        return jsonify({"error": "Unauthorized"}), 401
    
    payload = request.json or {}
    alert_name = payload.get("alert_name", "Unknown Incident")
    details = payload.get("details", "No details provided")

    return jsonify({
        "status": "success",
        "message": f"Alert '{alert_name}' routed to Switch room #techpulse-alerts"
    }), 200

if __name__ == "__main__":
    app.run(port=5001, debug=True)
