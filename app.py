# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Add each client here when they buy your module
CLIENTS = {
    "TEYA-CLIENT-A-2024": {"active": True},
    "TEYA-CLIENT-B-2024": {"active": True},
    "TEYA-CLIENT-C-2024": {"active": False},  # revoked
}

# Your real Teya credentials (only on YOUR server)
TEYA_CLIENT_ID = "bed6c087-6fb1-4747-9a92-9643c4b9c3cb"
TEYA_CLIENT_SECRET = "j16t5svGCB2C-ZqDNJ4yPp7jDsbEdaNaTMAgcRWon04"

@app.route("/api/credentials", methods=["POST"])
def get_credentials():
    data = request.json
    license_key = data.get("license_key")

    client = CLIENTS.get(license_key)

    if not client:
        return jsonify({"error": "Invalid license"}), 403

    if not client["active"]:
        return jsonify({"error": "License expired"}), 403

    return jsonify({
        "client_id": TEYA_CLIENT_ID,
        "client_secret": TEYA_CLIENT_SECRET
    })

if __name__ == "__main__":
    app.run()
