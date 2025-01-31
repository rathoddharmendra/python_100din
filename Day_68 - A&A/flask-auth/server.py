from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/login', methods=['GET'])
def login():
    return render_template("index.html")

@app.route('/register', methods=['GET'])
def register():
    return render_template("index.html")


if __name__ == "__main__":
    app.debug = True
    app.run()

