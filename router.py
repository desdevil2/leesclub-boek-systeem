from flask import Flask, render_template, request, redirect, session
from database import register_for_event, RegisterStatus, get_all_book_days, create_event, get_registered_for_event
from credentials import key
app = Flask(__name__)
app.config["SECRET_KEY"] = key

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
    if check_login():
        return render_template("create_event.html")
    else:
        return redirect("login")

@app.route("/create_event", methods=["POST"])
def create_event_post():
    if check_login():
        create_event(request.form)
        return "SUCCES"
    else:
        return "NOT LOGGED IN"

@app.route("/view_event", methods=["GET"])
def view_event():
    events = get_all_book_days()
    registered_people = get_registered_for_event(events[0]["id"])
    return render_template("view_event.html", events=events, registered_people=registered_people)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    name = request.form["name"]
    password = request.form["password"]
    if name == "abc" and password == "abc":
        session["name"] = "abc"
        return "SUCCES"
    else:
        return "NO"


def check_login():
    try:
        name = session["name"]
        return True
    except KeyError:
        return False


@app.route("/logout", methods=["POST"])
def logout():
    if check_login:
        session.pop("name", None)
    return "SUCCES"