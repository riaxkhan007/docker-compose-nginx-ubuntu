from flask import Flask, jsonify
import socket
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>Docker Compose Project</title>
        </head>
        <body>
            <h1>Welcome to My Docker Compose Project!</h1>
            <p>Flask application running successfully.</p>
            <p>Deployed on Ubuntu using Docker Compose and Nginx.</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now(timezone.utc).isoformat()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

