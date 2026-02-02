from flask import Flask, request, jsonify
import time
import logging
from collections import defaultdict

app = Flask(__name__)

# Security configuration
MAX_ATTEMPTS = 5
BLOCK_TIME = 300  # seconds

attempts = defaultdict(list)
blocked_ips = {}

# Logging setup
logging.basicConfig(
    filename="security.log",
    level=logging.WARNING,
    format="%(asctime)s - %(message)s"
)

@app.route("/login", methods=["POST"])
def login():
    ip = request.remote_addr
    now = time.time()

    # Check if IP is blocked
    if ip in blocked_ips and now < blocked_ips[ip]:
        logging.warning(f"BLOCKED IP tried access: {ip}")
        return jsonify({"status": "blocked"}), 403

    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Dummy credentials
    if username == "admin" and password == "password123":
        attempts[ip].clear()
        return jsonify({"status": "success"})

    # Record failed attempt
    attempts[ip].append(now)
    attempts[ip] = [t for t in attempts[ip] if now - t < 60]

    if len(attempts[ip]) >= MAX_ATTEMPTS:
        blocked_ips[ip] = now + BLOCK_TIME
        logging.warning(f"BRUTE FORCE detected from {ip}")
        return jsonify({"status": "blocked"}), 403

    logging.warning(f"FAILED login from {ip}")
    return jsonify({"status": "failed"}), 401


if __name__ == "__main__":
    print("🛡️ Brute-force detector running on http://127.0.0.1:5000")
    app.run(debug=False)
