from flask import Flask, render_template

app = Flask (__name__)

class_roster = [
    ("Grace", 90, "Junior"),
    ("John", 87, "Sophomore"),
    ("Travis", 79, "Senior"),
    ("Alexandra", 93, "Freshman"),
    ("Thomas", 70, "Freshman"),
    ("Herman", 82, "Freshman"),
    ("Allie", 67, "Junior")
    ]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name = student_name)

@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", class_roster = class_roster, grade_view = grade_view)


@app.route("/layout")
def layout():
    return render_template("layout.html")