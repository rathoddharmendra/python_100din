from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", message={'name': 'Dee', 'count': 12})

if __name__ == "__main__":
    app.run(debug=True)

