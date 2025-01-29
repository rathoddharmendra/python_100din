from flask import Flask, render_template, request
import requests
from conn import Connection  # Replace with your own SMTP connection class

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)
conn = Connection()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html", header_title="Contact Me")
    if request.method == "POST":
        data = request.form
        print(data)
        # Send email using your SMTP server or any other email service
        conn.send_email(to_address="rathoddharmendra.business@gmail.com", subject="New Message from Dee Bloggr Website", body=f"Name: {data['name']}\nEmail: {data['email']}\nPhone: {data['phone']}\nMessage: {data['message']}")
        return render_template("contact.html", header_title="Successfully Sent Your Message")
    
@app.route("/post/<int:index>")
def show_post(index: int):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
