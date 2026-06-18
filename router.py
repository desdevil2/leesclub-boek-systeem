from flask import Flask, render_template
from database import get_book_day
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/register")
def home():
    data = get_book_day(1)
    vars = {}
    # vars["book_title"] = "The hunger games"
    # vars["book_description"] = "lorum ipsum"
    # vars["capacity"] = 10
    # vars["registered_count"] = 7
    # vars["date"] = "01/04/2026"
    # vars["time"] = "19:00"
    # vars["location"] = "Meilweg 7, 3600 Genk"
    vars["capacity"] = data[1]
    vars["book_title"] = data[2]
    vars["book_description"] = data[3]
    vars["date"] = data[4]
    vars["time"] = data[5]
    vars["location"] = data[6]
    vars["registered_count"] = data[7]
    return render_template("register.html", **vars)