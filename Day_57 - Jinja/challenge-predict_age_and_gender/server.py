from flask import Flask, render_template, redirect
import datetime as dt
import requests

app = Flask(__name__)

CURRENT_YEAR = dt.datetime.now().strftime("%Y")

GENDER_BASE_URL = 'https://api.genderize.io/'
AGE_BASE_URL = 'https://api.agify.io/'


@app.route("/")
def home():
    return ""
@app.route("/guess/<string:name>")
def index(name: str):
    parameters = {"name": name}
    predicted_gender  = requests.get(GENDER_BASE_URL, params=parameters).json()['gender']
    predicted_age = requests.get(AGE_BASE_URL, params=parameters).json()['age']

    return render_template("index.html", 
                            name=name,
                            predicted_gender=predicted_gender,
                            predicted_age= predicted_age,
                            current_year=CURRENT_YEAR )

if __name__ == "__main__":
    app.run(debug=True)

