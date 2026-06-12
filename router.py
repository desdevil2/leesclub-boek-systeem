from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/register")
def home():
    vars = {}
    vars["book_title"] = "The hunger games"
    vars["book_description"] = "lorum ipsum"
    vars["capacity"] = 10
    vars["registered_count"] = 7
    vars["date"] = "01/04/2026"
    vars["time"] = "19:00"
    vars["location"] = "Meilweg 7, 3600 Genk"
    return render_template("register.html", **vars)