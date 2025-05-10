from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"service": "Backend 1", "message": "Hello from Backend 1!"})

if __name__  == '__main__':
    app.run(port=9001)