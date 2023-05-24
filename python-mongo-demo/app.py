from flask import Flask, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

mongo_host = os.getenv("MONGO_HOST", "localhost")
mongo_port = os.getenv("MONGO_PORT", "27017")

client = MongoClient(f"mongodb://{mongo_host}:{mongo_port}")
db = client["mydatabase"]

@app.route("/")
def hello():
    return jsonify({"message": "Hello, world!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
