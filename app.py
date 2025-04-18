from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Pathway Backend!"

@app.route("/status")
def status():
    return jsonify({"status": "Running", "message": "Pathway backend is live!"})

# You can add more routes here
