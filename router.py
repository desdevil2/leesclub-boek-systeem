from flask import Flask, render_template, request, redirect, jsonify
from database import get_book_day, register_for_event, is_registered, RegisterStatus, get_all_book_days
app = Flask(__name__)

@app.route("/")
def hello_world():
    return redirect("/register")

@app.route("/register")
def home():
    data = get_all_book_days()
    # vars["book_title"] = "The hunger games"
    # vars["book_description"] = "lorum ipsum"
    # vars["capacity"] = 10
    # vars["registered_count"] = 7
    # vars["date"] = "01/04/2026"
    # vars["time"] = "19:00"
    # vars["location"] = "Meilweg 7, 3600 Genk"

    return render_template("register.html", events=data)

@app.route("/register_for_event", methods=["POST"])
def register_for_event_post():
    email = request.form["email"]
    id = int(request.form["id"])
    status = register_for_event(id, email)
    if status == RegisterStatus.SUCCES:
        return "SUCCES"
    elif status == RegisterStatus.FULL:
        return "FULL"
    elif status == RegisterStatus.DUPLICATE:
        return "DUPLICATE"
    else:
        return "ERROR"


