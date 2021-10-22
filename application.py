import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)


# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    # edit_birthday= db.execute("SELECT FROM birthdays (id) VALUES (?)", id)
    edit_birthday = db.execute("SELECT id FROM birthdays")
    # birthdays.query.get(id)
    if request.method == "POST":
        edit_birthday.name = request.form['name']
        try:
            db.session.commit ()
            return redirect("/index")
        except:
            return "There was a problem updating your birthday"
    else:
        render_template("edit.html", edit_birthday=edit_birthday)



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        name = request.form.get("name")
        if not name:
            return render_template("index.html")

        month = request.form.get("month")
        if not month:
            return render_template("index.html")


        day = request.form.get("day")
        if not name:
            return render_template("index.html")

        db.execute ("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)
