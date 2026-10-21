from flask import Flask
import os

app = Flask(__name__)

SERVER_NAME = os.getenv("SERVER_NAME", "Unknown Server")


@app.route("/")
def home():
    return {
        "message": "Application is running!",
        "backend_server": SERVER_NAME
    }


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "backend_server": SERVER_NAME
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
