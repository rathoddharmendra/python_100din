from flask import Flask, render_template
import os

index_page_path =  os.path.join(os.path.dirname(__file__),'../pages/index.html')

app = Flask(__name__)

@app.route("/")
def main():
    return render_template(template_name_or_list='index.html',  
                           message='I\'m Dee')


@app.route("/resume")
def resume():
    return render_template(template_name_or_list='resume.html')

@app.route("/cv")
def cv():
    return render_template(template_name_or_list='cv.html')

if __name__ == "__main__":
    app.run(debug=True)