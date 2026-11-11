from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify(servico="SCN API", versao="1.0", status="ok")

@app.get("/health")
def health():
    return jsonify(status="healthy"), 200
