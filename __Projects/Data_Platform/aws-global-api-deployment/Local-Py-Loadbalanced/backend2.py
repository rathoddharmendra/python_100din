from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"service": "Backend 2", "message": "Hello from Backend 2!"})

if __name__  == '__main__':
    app.run(port=9002)