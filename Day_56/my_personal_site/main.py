from flask import Flask, render_template
import os

index_page_path =  os.path.join(os.path.dirname(__file__),'../pages/index.html')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template(template_name_or_list='index.html',  
                           message='I\'m Dee')

if __name__ == "__main__":
    app.run(debug=True)