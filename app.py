from flask import Flask, request, jsonify
import subprocess, os
app = Flask(__name__)

@app.route("/")
def index():
    return "Bridge OK"

@app.route("/exec", methods=["POST"])
def ex():
    if request.json.get("key") != "claude2025": return {}, 403
    r = subprocess.run(request.json.get("cmd",""), shell=True, capture_output=True, text=True, timeout=30)
    return {"out": r.stdout + r.stderr}
