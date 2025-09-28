from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message": "Mystic Forest Flow - Minimal Test", "status": "working"})

@app.route('/api/test')
def test():
    return jsonify({"message": "API test working", "timestamp": "test"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
