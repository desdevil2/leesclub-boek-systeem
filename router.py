from flask import Flask, render_template, request, redirect
from database import register_for_event, RegisterStatus, get_all_book_days, create_event
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
    name = request.form["name"]
    status = register_for_event(id, email, name)
    if status == RegisterStatus.SUCCES:
        return "SUCCES"
    elif status == RegisterStatus.FULL:
        return "FULL"
    elif status == RegisterStatus.DUPLICATE:
        return "DUPLICATE"
    else:
        return "ERROR"
    
@app.route("/create_event", methods=["GET"])
def create_event_get():
    return render_template("create_event.html")

@app.route("/create_event", methods=["POST"])
def create_event_post():
    create_event(request.form)
    return "SUCCES"


