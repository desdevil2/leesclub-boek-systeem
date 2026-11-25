from flask import Flask, render_template, request, redirect, session
from database import register_for_event, RegisterStatus, get_all_book_days, get_registered_for_event, validate_create_event_data, validate_register_data, create_event
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
    print(check_login())
    return render_template("register.html", events=data, login=check_login())

@app.route("/register_for_event", methods=["POST"])
def register_for_event_post():
    if validate_register_data(request.form):
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
    else:
        return "FAILURE"
    
@app.route("/create_event", methods=["GET"])
def create_event_get():
    if check_login():
        return render_template("create_event.html", login=True)
    else:
        return redirect("login")

@app.route("/create_event", methods=["POST"])
def create_event_post():
    if check_login():
        if validate_create_event_data(request.form, request.files):
            create_event(request.form, request.files)
            return "SUCCES"
        else:
            return "FAILURE"
    else:
        return "NOT LOGGED IN"

@app.route("/view_event", methods=["GET"])
def view_event():
    events = get_all_book_days()
    registered_people = get_registered_for_event(events[0]["id"])
    return render_template("view_event.html", events=events, registered_people=registered_people, login=check_login())


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html", login=check_login())


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


@app.route("/logout", methods=["GET", "POST"])
def logout():
    if check_login:
        session.pop("name", None)
    return redirect("/login")