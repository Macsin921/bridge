from flask import Flask, request, jsonify
import subprocess
import os
app = Flask(__name__)

@app.route("/")
def index():
    return "Bridge OK"

@app.route("/exec", methods=["POST"])
def ex():
    if request.json.get("key") != "claude2025":
        return {}, 403
    r = subprocess.run(request.json.get("cmd",""), shell=True, capture_output=True, text=True, timeout=30)
    return jsonify({"out": r.stdout + r.stderr})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host="0.0.0.0", port=port)
