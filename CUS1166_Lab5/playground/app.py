# Import appropriate libraries,
import sys
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# This module defines that database parameters.
from config import Config
# Load the models (i.e. Flights, Passenger model classes)
from models import *
# Define an instance of flask application, load database parameters.

app = Flask(__name__)
app.config.from_object(Config)
# SQLAlchemy class need an instance of the flask app to know of the application model.
db.init_app(app)
# Define a route

@app.route("/")
def index():
    courses = Course.query.all()
    return render_template('index.html', courses = courses)


@app.route("/add_course", methods=["post"])
def add_course():
    # Get information from the form.
    id = request.form.get("ID")
    number = request.form.get("number")
    title = request.form.get("title")

    # Equivalent to:
    # INSERT INTO flights (flight_number, origin, destination, durations) VALUES (origin,...)
    course = Course(id = id ,course_number= number, course_title = title)
    db.session.add(course)
    db.session.commit()
    # Query database.

    courses=Course.query.all()
    return render_template('index.html', courses = courses)


@app.route("/register_student/<int:course_id>", methods=["GET", "POST"])
def register_student(course_id):
        #
        # Equivalent to "SELECT * from flights where id=flight_id"
    course =Course.query.get(course_id)
        # If this is a post request = Add the passenger.
    if request.method == 'POST':
        #id = request.form.get("id")
        name =request.form.get("name")
        grade =request.form.get("grade")
            # Use the utility method to add a new passenger in the database.
        course.add_student(name, grade)
            # Use the relationships field in the flights model to retrieve
        # all passengers in the current flight.
    students = course.students
    return render_template("course_details.html", course = course, students = students)

            
def main():
    if (len(sys.argv) == 2):
        print(sys.argv)
    if sys.argv[1] == 'createdb':
        db.create_all()
    else:
        print("Run app using 'flask run'")
        print("To create a database use 'python app.py createdb")
        # Run the main method in the context of our flass application
        # This allows db know about our models.
        
if __name__ == "__main__":
     with app.app_context():
        main()
