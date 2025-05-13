from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "ok",
        "message": "Hello Cloud Foundry!"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

if __name__ == '__main__':
    # Get port from environment variable or choose 8080 as local default
    port = int(os.getenv("PORT", 8080))
    # Run the app
    app.run(host='0.0.0.0', port=port)