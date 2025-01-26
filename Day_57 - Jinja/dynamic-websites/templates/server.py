from flask import Flask, render_template
import datetime as dt

app = Flask(__name__)

CURRENT_YEAR = dt.datetime.now().strftime("%Y")

@app.route("/")
def index():

    return render_template("index.html", 
                            message={
                               'name': 'Dee Rathod', 
                               'count': 12, 
                               'url': "https://sheralkaren.github.io/git-pages/"}, 
                            year= CURRENT_YEAR )

if __name__ == "__main__":
    app.run(debug=True)

