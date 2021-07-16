from flask import Flask, render_template, redirect, request, flash
from mysqlconnection import connectToMySQL
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = "swordfish"
mysql = MySQLConnector(app, "justemails")
@app.route('/')
def index():
    return render_template('index.html')
@app.route("/check", methods=["POST"])
def check():
    em = request.form["email"]
    if not EMAIL_REGEX.match(em):
        flash("Email is not valid!")
        return redirect("/")
    elif request.form.get("delete"):
        emails = mysql.query_db("SELECT email FROM emails;")
        query = "DELETE FROM emails WHERE email = '{}'".format(em)
        
        for e in emails:
            if e["email"] == em:
                mysql.query_db(query)
                msg = "Email ({}) successfully deleted".format(em)
                flash(msg)
                return redirect("/success")
        msg = "Email ({}) not found in database".format(em)
        flash(msg)
        return redirect("/")
    else:
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES('{}', NOW(), NOW());".format(em)
        mysql.query_db(query)
        msg = "The email address you entered ({}) is a VALID email address! Thank you!".format(em)
        flash(msg)
        return redirect("/success")
@app.route("/success")
def success():
    emails = mysql.query_db("SELECT email, updated_at FROM emails;")
    return render_template("success.html", emails=emails)
app.run(debug=True)